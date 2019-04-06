from dataaccess.dataaccesslayer import DataAccessLayer
from models.link_stations import LinkStations
from services.compute import ComputeMostSuitable
from models.device import Device
from json import dumps
from flask import make_response

compute = ComputeMostSuitable(
    LinkStations(DataAccessLayer())
)


def computedevice(request):
    """HTTP Cloud Function.
    Parameters:
        request (flask.Request): The request object.
        if in query string the x and y are present as valid coordinates it will process that point
        otherwise if no args are passed in the query string it will process the standard points
        (0,0), (100, 100), (15,10) and (18, 18).
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        A json array compose by the strings:
        “Best link station for point x,y is x,y with power z”
        Or
        “No link station within reach for point x,y”
    """
    # All the print are logged automatically on stackdriver

    x_args = request.args.get('x')
    y_args = request.args.get('y')

    if not x_args or not y_args:
        print('the query string is not in the expected format or is empty', request)
        devices_to_process = [
            Device(0, 0),
            Device(100, 100),
            Device(15, 10),
            Device(18, 18)
        ]
    else:
        try:
            x = float(x_args)
            y = float(y_args)
        except ValueError as vError:
            print('the x and y params inputs are not valid coordinates', vError)
            return 'the X and Y inputs are not valid coordinates (float)'
        else:
            devices_to_process = [Device(x, y)]

    results = []
    for device_to_process in devices_to_process:
        max_power, station_point = compute.process_suitable_link(
            device_to_process)

        if (max_power > 0):
            result = f'Best link station for point {device_to_process.get_x()},{device_to_process.get_y()} is {station_point[0]},{station_point[1]} with power {max_power}'
        else:
            result = f'No link station within reach for point {device_to_process.get_x()},{device_to_process.get_y()}'

        print(result)
        results.append(result)

    # flask.jsonify doesn't allow to serialize list
    # https://github.com/pallets/flask/issues/170
    return make_response(dumps(results))
