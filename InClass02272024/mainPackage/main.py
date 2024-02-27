'''
main.py
'''

# Add an import statement for Vehicle class
from VehiclePackage.VehicleClass import *

if __name__ == "__main__":
    # Instantiate an object of Type Vehicle
    myCorvette = Vehicle("Car", 120) # Trigger a call to the constructor 
    myCorvette.printType() # Invoke the method on the object
    
    # Invoke the getter for maximum speed, store the return value in a variable and print to console
    maximum_speed = myCorvette.getSpeed()
    print ("Maximum Speed:", maximum_speed)
    
    # Instantiate another Vehicle object. You make up name
    myCorolla = Vehicle("Car")  # myCorolla is an object of type Vehicle
    
    
    # I want a list of 3 vehicles: Car, Boat, and Space Ship 
    # Pick the names and properties 
    
    myVehicles = [Vehicle("Corvette", 120),Vehicle("Pontoon", 20),Vehicle("Tie Fighter", 500)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
        
    myCorvette = Vehicle("Car",120)
    maximum_speed = myCorvette.getSpeed
    myCorvette.printType()
    print ("Maximum Speed:", maximum_speed)
    
    myPontoon = Vehicle("Boat", 20)
    maximum_speed = myPontoon.getSpeed()
    myPontoon.printType()
    print ("Maximum Speed:", maximum_speed)
    
    myTieFighter = Vehicle("Space Ship", 500)
    maximum_speed = myTieFighter.getSpeed()
    myTieFighter.printType()
    print ("Maximum Speed:", maximum_speed)

    