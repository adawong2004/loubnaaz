class vehicle :
    def __init__(self,make,model):
        self.make=make
        self.model=model

class car(vehicle):
    def __init__(self,make,model,doors):
        self.doors=doors
        super(). __init__(make,model)

class ElectricCar(car):
    def __init__(self,doors,battery_range):
        self.battery_range=battery_range
        super(). __init__(doors)

    def displaydaitails ():
        print()      
        