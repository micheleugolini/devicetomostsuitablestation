from abc import ABC, abstractmethod
import numpy as np
from helpers.calculations import nearest_point, link_station_power
from models.link_stations import IStations
from models.device import IDevice


class IComputeMostSuitable(ABC):

    @abstractmethod
    def process_suitable_link(self, device: IDevice):
        """
        Process the most powerful link between the device and the stations

        Parameters:
            device_point (IDevice): The device to process for the most suitable link

        Returns:
            max_power (float): the max power link between the device and the station, if 0 no available link within reach
            station_point ([x, y]): the coordinates of the station with max power for the device_point
        """
        pass


class ComputeMostSuitable(IComputeMostSuitable):

    def __init__(self, linkstations: IStations):
        self.__available_stations = linkstations
        super().__init__()

    # Eventually we can pass also the function to calculate the link to station power,
    # so if the formula change we just need to pass a different function,
    # for the moment I considered the formula as a constant
    def process_suitable_link(self, device: IDevice):
        """
        Process the most powerful link between the device and the stations

        Parameters:
            device_point (IDevice): The device to process for the most suitable link

        Returns:
            max_power (float): the max power link between the device and the station, if 0 no available link within reach
            station_point ([x, y]): the coordinates of the station with max power for the device_point
        """
        coordinates, reaches = self.__get_coordinates_and_reaches()
        return self.__process_suitable_link(device.get_point(), coordinates, reaches)

    def __get_coordinates_and_reaches(self):
        """
        Function load the stations from the data access layer and return the station coordinates and station reaches

        Returns:
            stations_coordinates (numpy.array [[x1, y1], [x2,y2], ...]): The stations coordinates
            stations_reaches (numpy.array [r1, r2, ...]): The station reach
        """
        return self.__available_stations.get_coordinates(), self.__available_stations.get_reaches()

    def __process_suitable_link(self, device_point, stations_coordinates, stations_reaches, max_power=0, station_point=[0, 0]):
        """
        Recursive function that process the most powerful link between the device and the stations
        the indexes of the stations_coordinates have to match the indexes of the station_reaches

        Parameters:
            device_point ([x, y]): The device coordinates
            stations_coordinates (numpy.array [[x1, y1], [x2,y2], ...]): The stations coordinates
            stations_reaches (numpy.array [r1, r2, ...]): The station reach
            max_power (float): Used for recursion, is the max power link
            station_point ([x, y]): used for recursion is the coordinates of the station with max power for the device_point

        Returns:
            max_power (float): the max power link between the device and the station, if 0 no available link within reach
            station_point ([x, y]): the coordinates of the station with max power for the device_point
        """
        if (len(stations_reaches) < 1):
            return max_power, station_point

        distance, index, current_station = nearest_point(
            device_point, stations_coordinates)
        if distance > max(stations_reaches):
            if (max_power > 0):
                return max_power, station_point
            else:
                return 0, None
        else:
            current_power = link_station_power(
                stations_reaches[index], distance)
            stations_reaches = np.delete(stations_reaches, index)
            stations_coordinates = np.delete(
                stations_coordinates, index, axis=0)

            if (max_power < current_power):
                return self.__process_suitable_link(device_point, stations_coordinates, stations_reaches, current_power, current_station)
            else:
                return self.__process_suitable_link(device_point, stations_coordinates, stations_reaches, max_power, station_point)
