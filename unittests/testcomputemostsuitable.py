import unittest
from dataaccess.dataaccesslayer import DataAccessLayer
from services.compute import ComputeMostSuitable
from models.link_stations import LinkStations
from models.device import Device

# we actually should use a mock up data access layer to perform
# test but in this case the data access layer is already a mock up one
link_stations = LinkStations(DataAccessLayer())


class TestCompute(unittest.TestCase):

    def setUp(self):
        self.compute = ComputeMostSuitable(link_stations)

    def test_device_0_0(self):
        max_power, station_point = self.compute.process_suitable_link(
            Device(0, 0))
        self.assertEqual(
            max_power, 100, msg='wrong max_power calculation for device(0,0)')
        # another option would be to use np.testing.assert_array_equal
        self.assertEqual(station_point[0], 0,
                         msg='the X coordinate station is not the most suitable for device(0,0)')
        self.assertEqual(station_point[1], 0,
                         msg='the Y coordinate station is not the most suitable for device(0,0)')

    def test_device_100_100(self):
        max_power, station_point = self.compute.process_suitable_link(
            Device(100, 100))
        self.assertEqual(
            max_power, 0, msg='there is not a most suitable link to device(100, 100)')

    def test_device_20_20(self):
        max_power, station_point = self.compute.process_suitable_link(
            Device(20, 20))
        self.assertEqual(
            max_power, 25, msg='wrong max_power calculation for device(20,20)')
        # another option would be to use np.testing.assert_array_equal
        self.assertEqual(station_point[0], 20,
                         msg='the X coordinate station is not the most suitable for device(20,20)')
        self.assertEqual(station_point[1], 20,
                         msg='the Y coordinate station is not the most suitable for device(20,20)')
