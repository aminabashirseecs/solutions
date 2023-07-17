import unittest
from datetime import date, timedelta
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class CarTestCase(unittest.TestCase):
    def setUp(self):
        self.today = date.today()
        self.one_year_ago = self.today - timedelta(days=365)
        self.three_years_ago = self.today - timedelta(days=3 * 365)
        self.five_years_ago = self.today - timedelta(days=5 * 365)

    def test_battery_needs_service(self, CarClass):
        car = CarClass(self.three_years_ago, 0, 0)
        self.assertTrue(car.needs_service())

    def test_battery_does_not_need_service(self, CarClass):
        car = CarClass(self.one_year_ago, 0, 0)
        self.assertFalse(car.needs_service())

    def test_engine_needs_service(self, CarClass):
        car = CarClass(self.today, 30001, 0)
        self.assertTrue(car.needs_service())

    def test_engine_does_not_need_service(self, CarClass):
        car = CarClass(self.today, 30000, 0)
        self.assertFalse(car.needs_service())


class TestCalliope(CarTestCase):
    def setUp(self):
        super().setUp()
        self.CarClass = Calliope


class TestGlissade(CarTestCase):
    def setUp(self):
        super().setUp()
        self.CarClass = Glissade


class TestPalindrome(CarTestCase):
    def setUp(self):
        super().setUp()
        self.CarClass = Palindrome


class TestRorschach(CarTestCase):
    def setUp(self):
        super().setUp()
        self.CarClass = Rorschach


class TestThovex(CarTestCase):
    def setUp(self):
        super().setUp()
        self.CarClass = Thovex


if __name__ == '__main__':
    unittest.main()
