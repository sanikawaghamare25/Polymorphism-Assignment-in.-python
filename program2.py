2. Write a Java program to create a base class Animal (Animal Family) with a method called Sound(). Create two subclasses Bird and Cat. Override the Sound() method in each subclass to make a specific sound for each animal.


class Animal:
    def sound(self):
        print("animal class function")


class Cat(Animal):
    def display(self):
        super().sound()
        cat_sound="maau..maau"
        print("Cat sount=",cat_sound)


class Bird(Animal):
    def display(self):
        super().sound()
        bird_sound="chiiv..chivv"
        print("bird sound=",bird_sound)


e=Cat()
e. display()
a=Bird()
a.display()
