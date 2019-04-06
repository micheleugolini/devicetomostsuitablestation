from services.compute import ComputeMostSuitable
from dataaccess.dataaccesslayer import DataAccessLayer
from models.link_stations import LinkStations
from models.device import Device
import sys


def get_user_input_device():
    user_input_x = input('Enter the X for the device you want to process: ')
    user_input_y = input('Enter the Y for the device you want to process: ')
    try:
        x = float(user_input_x)
        y = float(user_input_y)
        return Device(x, y)
    except ValueError:
        print('The inputs are not valid coordinates')
        return sys.exit(0)


if __name__ == "__main__":
    y_or_n = input(
        'Do you want to insert the device point (Y) or process the default devices (N)? (Y/N) ').lower()
    if (y_or_n != 'y' and y_or_n != 'n'):
        print('Only Y or N are valid')
        sys.exit(0)
    if (y_or_n == 'y'):
        devices_to_process = [get_user_input_device()]
    else:
        devices_to_process = [
            Device(0, 0),
            Device(100, 100),
            Device(15, 10),
            Device(18, 18)
        ]

    link_stations = LinkStations(DataAccessLayer())
    compute = ComputeMostSuitable(link_stations)
    for device_to_process in devices_to_process:
        max_power, station_point = compute.process_suitable_link(
            device_to_process)
        if (max_power > 0):
            print(
                f'Best link station for point {device_to_process.get_x()},{device_to_process.get_y()} is {station_point[0]},{station_point[1]} with power {max_power}')
        else:
            print(
                f'No link station within reach for point {device_to_process.get_x()},{device_to_process.get_y()}')
