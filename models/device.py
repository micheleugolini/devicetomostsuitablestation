from abc import ABC, abstractmethod


class IDevice(ABC):

    @abstractmethod
    def get_x(self):
        """
        Get the X coordinate

        Returns:
            x (float): The X coordinate of the device
        """
        pass

    @abstractmethod
    def get_y(self):
        """
        Get the Y coordinate

        Returns:
            y (float): The Y coordinate of the device
        """
        pass

    @abstractmethod
    def get_point(self):
        """Get the device point in coordinates [x,y]"""
        pass


class Device(IDevice):

    def __init__(self, x, y):
        """
        Constructor for the implementation of IDevice as Device

        Parameters:
            x(float): The X coordinate of the device
            y(float): The Y coordinate of the device
        """
        self.__x = x
        self.__y = y
        super().__init__()

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_point(self):
        return [self.__x, self.__x]
