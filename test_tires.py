import unittest
from tires.carrigan import CarriganTires
from tires.octoprime import OctoprimeTires

class TestTires(unittest.TestCase):
    def test_carrigan_tires(self):
        tire = CarriganTires([0.8, 0.8, 0.9, 0.8]) # one value is larger than or equal to 0.9
        self.assertTrue(tire.needs_service())
        
        tire = CarriganTires([0.6, 0.5, 0.2, 0.4]) # No value is larger than or equal to 0.9
        self.assertFalse(tire.needs_service())
        
    def test_octoprime_tires(self):
        tire = OctoprimeTires([0.3, 0.3, 0.2, 0.3]) # The sum is less than 3
        self.assertFalse(tire.needs_service())
        
        tire = OctoprimeTires([0.7, 0.4, 0.9, 1.0]) # The sum is equal to 3
        self.assertTrue(tire.needs_service())
        
        tire = OctoprimeTires([0.8, 0.6, 0.9, 1.0]) # The sum is larger than 3
        self.assertTrue(tire.needs_service())
        
        
if __name__ == '__main__':
    unittest.main()