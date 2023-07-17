import unittest
from datetime import date, timedelta
from engine.model.calliope import Calliope


class TestCalliope(unittest.TestCase):
    def setUp(self):
        self.today = date.today()
        self.one_year_ago = self.today - timedelta(days=365)
        self.three_years_ago = self.today - timedelta(days=3 * 365)
        self.five_years_ago = self.today - timedelta(days=5 * 365)

    def test_battery_needs_service(self):
        car = Calliope(self.three_years_ago, 0, 0)
        self.assertTrue(car.needs_service())

    def test_battery_does_not_need_service(self):
        car = Calliope(self.one_year_ago, 0, 0)
        self.assertFalse(car.needs_service())

    def test_engine_needs_service(self):
        car = Calliope(self.today, 30001, 0)
        self.assertTrue(car.needs_service())

    def test_engine_does_not_need_service(self):
        car = Calliope(self.today, 30000, 0)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
