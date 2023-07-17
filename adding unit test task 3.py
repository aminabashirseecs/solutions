import unittest
from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
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
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_create_glissade(self):
        car = CarFactory.create_glissade(self.current_date, self.last_service_date, self.current_mileage,
                                         self.last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_create_palindrome(self):
        car = CarFactory.create_palindrome(self.current_date, self.last_service_date, False)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_create_rorschach(self):
        car = CarFactory.create_rorschach(self.current_date, self.last_service_date, self.current_mileage,
                                          self.last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)

    def test_create_thovex(self):
        car = CarFactory.create_thovex(self.current_date, self.last_service_date, self.current_mileage,
                                       self.last_service_mileage)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, NubbinBattery)


if __name__ == '__main__':
    unittest.main()
