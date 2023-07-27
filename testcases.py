import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestEngines(unittest.TestCase):

    def test_capulet_engine(self):
        engine = CapuletEngine(30000, 60001) 
        self.assertTrue(engine.needs_service()) # Mileage under threshold
        
        engine = CapuletEngine(30000, 40000)
        self.assertFalse(engine.needs_service()) # Mileage over threshold

    def test_sternman_engine(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service()) # Light off
        
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service()) # Light on
        
    def test_willough_engine(self):
        engine = WilloughbyEngine(10000, 80000)
        self.assertTrue(engine.needs_service()) #
        engine = WilloughbyEngine(10000, 20000)
        self.assertFalse(engine.needs_service()) #

# tests/test_batteries.py

from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery

class TestBatteries(unittest.TestCase):

    def test_spindler_battery(self):
        from datetime import date
        
        battery = SpindlerBattery(date(2022, 1, 1), date(2023, 12, 31))
        self.assertFalse(battery.needs_service()) # Less than 2 year
        
        battery = SpindlerBattery(date(2022, 1, 1), date(2024, 1, 1)) 
        self.assertTrue(battery.needs_service()) # More than 2 year

    def test_nubbin_battery(self):
        # Similar tests for NubbinBattery
        from datetime import date
        
        battery = NubbinBattery(date(2022, 1, 1), date(2024, 12, 31))
        self.assertFalse(battery.needs_service()) # Less than 4 year
        
        battery = NubbinBattery(date(2022, 1, 1), date(2026, 1, 2)) 
        self.assertTrue(battery.needs_service()) # More than 4 year


if __name__ == '__main__':
    unittest.main()