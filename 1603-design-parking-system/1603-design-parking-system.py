class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big, self.medium, self.small = big, medium, small
                
    
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big -=1
            return True if self.big >= 0 else False
        if carType == 2:
            self.medium -=1
            return True if self.medium >= 0 else False
        self.small -=1
        return True if self.small >= 0 else False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)