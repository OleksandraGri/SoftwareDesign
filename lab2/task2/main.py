from abc import ABC, abstractmethod

#Базовий інтерфейс для створення девайсів
class Device(ABC):
    @abstractmethod
    def get_device_details(self):
        pass

#Конкретні девайси
class Laptop(Device):
    def get_device_details(self):
        return "Laptop: Powerful and portable"

class Netbook(Device):
    def get_device_details(self):
        return "Netbook: Small and lightweight"

class EBook(Device):
    def get_device_details(self):
        return "EBook: A digital reader for books"

class Smartphone(Device):
    def get_device_details(self):
        return "Smartphone: Mobile and versatile"

#Абстрактна фабрика для брендів
class DeviceFactory(ABC):
    @abstractmethod
    def create_device(self):
        pass

#Конкретні фабрики для брендів
class IProneFactory(DeviceFactory):
    def create_device(self):
        return Laptop()

class KiaomiFactory(DeviceFactory):
    def create_device(self):
        return Netbook()

class BalaxyFactory(DeviceFactory):
    def create_device(self):
        return Smartphone()

def main():
    iprone_factory = IProneFactory()
    device = iprone_factory.create_device()
    print(device.get_device_details())

if __name__ == "__main__":
    main()
