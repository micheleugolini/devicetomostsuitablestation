from abc import ABC, abstractmethod
import numpy as np
from dataaccess.dataaccesslayer import IDataAccessLayer


class IStations(ABC):

    @abstractmethod
    def get_coordinates(self):
        """
        Retrieve the coordinates without modify the stations

        Returns:
            The array of coordinates of the stations,
            if no station are loaded it returns an empty array
        """
        pass

    @abstractmethod
    def get_reaches(self):
        """
        Retrieve the reaches without modify the stations

        Returns:
            the array of the reaches of the stations,
            if no station are loaded it returns an empty array
        """
        pass


class LinkStations(IStations):

    def __init__(self, dataaccesslayer: IDataAccessLayer):
        """
        Constructor for the implementation of IStations as LinkStations

        Parameters:
            dataaccesslayer(IDataAccessLayer): The data access layer needed to load the stations
        """
        self.__stations = dataaccesslayer.get_stations()
        super().__init__()

    def get_coordinates(self):
        if len(self.__stations) > 0:
            return np.delete(np.copy(self.__stations), 2, 1)
        else:
            return []

    def get_reaches(self):
        if len(self.__stations) > 0:
            return np.copy(self.__stations)[:, 2]
        else:
            return []
