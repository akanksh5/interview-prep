from enum import Enum
from collections import defaultdict

class LockerSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Customer:
    def __init__(self,customer_id,name,email):
        self.customer= customer_id
        self.name = name
        self.email =email

class Package:
    def __init__(self,tracking_id, size: LockerSize, customer: Customer):
        self.tracking_id = tracking_id
        self.size = size
        self.customer = customer

class Locker:
    def __init__(self,locker_id,size: LockerSize):
        self.locker_id = locker_id
        self.size = size
        self.package = None
    
    def add_package(self,package:Package):
        if not self.package:
            self.package = package
            return True
        return False
    
    def release_package(self):
        if self.package:
            released_package = self.package
            self.package = None
            return released_package
        return None

class LockerSystem:
    def __init__(self):
        self.lockers = defaultdict(list)
        self.packages = {}
    
    def add_locker(self,locker: Locker):
        self.lockers[locker.size].append(locker)
    
    def find_available_locker(self,package: Package):
        for locker in self.lockers[package.size]:
            if locker.package is None:
                return locker
        print("No lockers available")
        return None

    def deliver_package(self,package: Package):
        locker: Locker = self.find_available_locker(package)
        if locker:
            locker.add_package(package)
            self.packages[package.tracking_id] = locker 
            print(f"Package with the id {package.tracking_id} is placed in the locker {locker.locker_id}")
        else:
            print(f"No lockers available currently.")
    
    def pickup_package(self,tracking_id,customer: Customer):
        if tracking_id in self.packages:
            locker: Locker = self.packages[tracking_id]
            if locker.package.customer == customer:
                locker.release_package()
                del self.packages[tracking_id]
                print(f"Package {tracking_id} has been picked up by the customer{customer.id}")
                return True
        print(f"Package not found or not authorized")
        return False


    