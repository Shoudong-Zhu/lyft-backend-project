import unittest
# tests/test_batteries.py

from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery

class TestBatteries(unittest.TestCase):

    def test_spindler_battery(self):
        from datetime import date
        
        battery = SpindlerBattery(date(2022, 1, 1), date(2023, 12, 31))
        self.assertFalse(battery.needs_service()) # Less than 3 year
        
        battery = SpindlerBattery(date(2022, 1, 1), date(2025, 1, 1)) 
        self.assertTrue(battery.needs_service()) # More than 3 year

    def test_nubbin_battery(self):
        # Similar tests for NubbinBattery
        from datetime import date
        
        battery = NubbinBattery(date(2022, 1, 1), date(2024, 12, 31))
        self.assertFalse(battery.needs_service()) # Less than 4 year
        
        battery = NubbinBattery(date(2022, 1, 1), date(2026, 1, 2)) 
        self.assertTrue(battery.needs_service()) # More than 4 year


if __name__ == '__main__':
    unittest.main()