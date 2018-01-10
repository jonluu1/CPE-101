import unittest
import vehicle

class VehicleTests(unittest.TestCase):
    def test_vehicle(self):
        testVehicle = vehicle.Vehicle(4, 10, 4, True)
        self.assertEquals(testVehicle.wheels, 4)
        self.assertEquals(testVehicle.fuel, 10)
        self.assertEquals(testVehicle.doors, 4)
        self.assertEquals(testVehicle.roof, True)
      # Add code here.


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

