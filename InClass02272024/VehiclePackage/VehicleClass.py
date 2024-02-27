'''
Vehicle class in VehicleClass.py
'''

class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Change Order: we need to add maximum speed to the model
    Change Order: we need a way to 'read' the maximum speed from the model
    Change Order: some developers need to use the constructor without having to provide maximum speed 
    '''
    # Constructor. It's called when... you create/instantiate an object of Vehicle type
    def __init__(self, type, max_speed = None):
        '''
        @Param type: The kind of vehicle
        @Param max_speed: Maximum speed of the vehicle, defaults to None 
        '''
        self.type = type;    # This encapsulates the type
        self._thisisprivate = 42  # This is a weak attempt to "support" data hiding (THE UNDERSCORE)
        self.max_speed = max_speed  # Save a copy in the current object

    # An instance method: It operates on an instance of the vehicle class
    def printType(self):
        print(self.type);
 
    def getSpeed(self):   # A GETTER
        return self.max_speed 
    
if __name__ == "__main__":
# Some code to test the class would go here.
# If there's no code, just pass
    pass


    