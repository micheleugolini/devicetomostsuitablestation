from scipy import spatial


def nearest_point(point, array_of_points):
    """
    Function that calculate the nearest point between the input point and a numpy.array of coordinates

    Parameters:
        point ([x, y]): The device coordinates
        array_of_points (numpy.array [[x1, y1], [x2, y2], ...]): The array of coordinates

    Returns:
        distance (float): the distance between the point and the nearest point of the coordinates array
        index (int): the index of the nearest point in the array of coordinates
        array_of_points[index] ([x, y]): the nearest to point in the array
    """
    distance, index = spatial.KDTree(array_of_points).query(point)
    return distance, index, array_of_points[index]


def link_station_power(reach, distance):
    """
    Function that calculate the power within reach based on the distance between the device and the station

    Parameters:
        reach: the reach of the station
        distance: the distance between the device and the station

    Returns:
        The power within reach based on the distance
    """
    return (reach - distance)**2
