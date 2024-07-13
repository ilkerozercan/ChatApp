
class ModuleSettings:
    def __init__(self):
        self.volume = 50
        
    def set_volume(self, value: int):
        if 0 < value and value < 100:
            self.volume = value
            return self.volume
        else:
            raise Exception(f"Value must be between 0 and 100 | Current Volume: {self.volume} | Parameter Value: {value}")
        
    
    def get_volume(self):
        return self.volume

    

