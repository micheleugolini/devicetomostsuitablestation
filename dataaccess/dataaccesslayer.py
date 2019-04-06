from abc import ABC, abstractmethod
import numpy as np


class IDataAccessLayer(ABC):
    @abstractmethod
    def get_stations(self):
        """
        Method to load the data of the stations

        Returns:
            The matrix of the link stations
        """
        pass


class DataAccessLayer(IDataAccessLayer):
    # If we would in future get this data from different sources
    # we can modify the DataAccessLayer class and the implementation
    # of get_stations to fetch data from somewhere else (e.g. file, db, etc...)
    def get_stations(self):
        return np.array([[0, 0, 10], [20, 20, 5], [10, 0, 12]])
