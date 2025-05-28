3. Write a python program to create a class Vehicle with a method called speedUp(). Create two subclasses Car and Bicycle. Override the speedUp() method in each subclass to increase the vehicle's speed differently.


class Vehical:
    def speedUp(self):
        print("speed of vehicals:")


class Car(Vehical):
    def speed(self):
        super().speedUp()
        car_speed=240
        print("car speed=",car_speed)


class Bicycle(Vehical):
    def speed(self):
        super().speedUp()
        Bicycle_speed=40
        print("Bicycle speed=",Bicycle_speed)


e=Car()
e.speed()


p=Bicycle()
p.speed()
