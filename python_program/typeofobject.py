class vehicle:
 def __init__(self, name, mileage, capacity):
    self.name = name
    self.mileage = mileage
    self.capacity = capacity

class Bus(vehicle):
  pass

school_bus = Bus("school volvo", 20, 50)
print(type(school_bus))