from datetime import datetime

class VehicleSize:
    MOTORCYCLE = 1
    CAR =  2 
    BUS = 3

class Vehicle:
    def __init__(self,license_plate,size):
        self.license_plate = license_plate
        self.size = size

class Motorcycle(Vehicle):
    def __init__(self,license_plate):
        self.license_plate = license_plate
        self.size = VehicleSize.MOTORCYCLE

class Car(Vehicle):
    def __init__(self,license_plate):
        self.license_plate = license_plate
        self.size = VehicleSize.CAR

class Bus(Vehicle):
    def __init__(self,license_plate):
        self.license_plate = license_plate
        self.size = VehicleSize.BUS

class Ticket:
    def __init__(self,vehicle,spot,entry_time):
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = entry_time
        self.exit_time = None
    
    def calculate_price(self,hourly_rate):
        self.exit_time = datetime.now()
        duration = (self.exit_time - self.entry_time).total_seconds() // 3600
        return round(duration*hourly_rate,2)

class ParkingSpot:
    def __init__(self,spot_id,size):
        self.spot_id = spot_id
        self.size = size
        self.is_free = True
        self.vehicle = None

    def can_fit_vehicle(self,vehicle):
        return self.is_free and self.size >= vehicle.size
    
    def park_vehicle(self,vehicle):
        if self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            self.is_free = False
            return True
        return False

    def remove_vehicle(self):
        if not self.is_free:
            vehicle = self.vehicle
            self.vehicle = None
            self.is_free = True
            return vehicle
        return None


class ParkingLot:
    def __init__(self,rates):
        self.spots = []
        self.parkedVehicles = {}
        self.rates = rates
    
    def park_vehicle(self,vehicle):
        for spot in self.spots:
            if spot.is_free and spot.can_fit_vehicle(vehicle):
                vehicle = spot.park_vehicle()
                ticket = Ticket(vehicle,spot,datetime.now())
                self.parkedVehicles[vehicles] = ticket
                print(f"Vehicle {vehicle.license_plate} is now parked at spot {spot.spot_id}")
                return ticket
        print(f"No available parking spots for the time being.")
    
    def remove_vehicle(self,license_plate):
        if license_plate in self.parkedVehicles:
            ticket = self.parkedVehicles.pop(license_plate)
            ticket.spot.remove_vehicle()
            fee = ticket.calculate_price(self.rates[ticket.vehicle.size])
            print(f"Total cost of the ticket is {fee}")
        else:
            print(f"Vehicle number with the license plate {license_plate} not found.")