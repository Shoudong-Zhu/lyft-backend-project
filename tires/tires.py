from abc import ABC
class Tires(ABC):
    def __init__(self, wear_array):
        self.wear_array = wear_array
        
    def needs_service(self):
        pass