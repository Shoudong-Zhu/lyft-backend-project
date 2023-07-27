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



if __name__ == '__main__':
    unittest.main()