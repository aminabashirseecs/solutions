import unittest
from datetime import date
from car_factory import CarFactory


class TestCarFactory(unittest.TestCase):
    def setUp(self):
        self.current_date = date.today()
        self.last_service_date = date.today()
        self.current_mileage = 0
        self.last_service_mileage = 0

    def test_create_calliope(self):
        car = CarFactory.create_calliope(self.current_date, self.last_service_date, self.current_mileage,
                                         self.last_service_mileage)
        self.assertIsNotNone(car)
        self.assertEqual(car.battery.service_interval, 3)  # Check upgraded battery service interval

    # Add other test methods for other car models


if __name__ == '__main__':
    unittest.main()
