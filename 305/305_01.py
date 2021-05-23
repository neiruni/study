from abc import ABCMeta, abstractmethod


class CarParent():
    def __init__(self, type, fuel, battery):
        self.type = type
        self.fuel = fuel
        self.battery = battery

    def run_func(self):
        distance = self.rotation_func(self.fuel, self.battery) * 10
        print('{0} 燃料{1} バッテリー{2} {3:,}km走る'.format(self.type, self.fuel, self.battery, distance))
 

class CarPower(CarParent, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, type, fuel, battery):
        super().__init__(type, fuel, battery)

    def rotation_func(self, fuel, battery):
        rotation = (fuel * 100) + (battery * 500)
        return rotation


class Car(CarPower):
    def __init__(self, type, fuel, battery):
        super().__init__(type, fuel, battery)


class HV(CarPower):
    def __init__(self, type, fuel, battery):
        super().__init__(type, fuel, battery)

    def Refueling_func(self):
        pass


class EV(CarPower):
    def __init__(self, type, fuel, battery):
        super().__init__(type, fuel, battery)
    
    def charging_func(self):
        pass



Car1 = Car('Car', 100, 0)
Car1.run_func()

HV1 = HV('HV', 50, 50)
HV1.run_func()

EV1 = EV('EV', 0, 100)
EV1.run_func()

