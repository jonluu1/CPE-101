import unittest
import vehicle

class VehicleTests(unittest.TestCase):
    def test_vehicle(self):
        testVehicle = vehicle.Vehicle(4, 10, 4, True)
        self.assertEquals(testVehicle.wheels, 4)
        self.assertEquals(testVehicle.fuel, 10)
        self.assertEquals(testVehicle.doors, 4)
        self.assertEquals(testVehicle.roof, True)

    def test_vehicle_again(self):
        testVehicle2 = vehicle.Vehicle(18, 100, 2, False)
        self.assertEquals(testVehicle2.wheels, 18)
        self.assertEquals(testVehicle2.fuel, 100)
        self.assertEquals(testVehicle2.doors, 2)
        self.assertEquals(testVehicle2.roof, False)
    # Add code here.


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

