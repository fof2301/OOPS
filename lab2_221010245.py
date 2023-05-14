#task 1
class Shape():
    def __init__(self,color):
        self.color=color
    def display_color(self):
        print(self.color)
class Circle(Shape):
    def __init__(self,color,radius,):
        super().__init__(color)
        self.radius=radius
    def display_color(self):
        print(self.color)
        print(self.radius)   
c1=Circle("red",10)
c1.display_color()

#task 2
class Vehicle():
    def __init__(self,brand):
        self.brand=brand
    def display_brand(self):
        print(self.brand)    
class Car(Vehicle):
    def __init__(self,brand):
        super().__init__(brand)
        
    def drive(self):
        return "Car is being driven"  
class SportsCar(Car):
    def __init__(self,brand):
        super().__init__(brand)
    def accelerate(self):
        return "Sports car accelerates."
c2=Car("volvo")
print(c2.drive())
c3=SportsCar("Lambo")
print(c3.accelerate())

#task3
class Animal():
    def __init__(self,name):
        self.name=name
    def speaks(self):
        return "Animal speaks"
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        return "Bark"
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        return "meow"
cat =Cat("Dexter")
dog= Dog("Bruno")
print(dog.speaks())
print(dog.make_sound())
print(cat.speaks())
print(cat.make_sound())

#task4

class A():
    def method_a():
        print("Method A from class A")
class B():
    def method_b():
        print("Method B from class B")
class C(A,B):
    def method_c():
        print("Method C from class C")
instance_Of_Class_C=C
instance_Of_Class_C.method_a()
instance_Of_Class_C.method_b()
instance_Of_Class_C.method_c()        

                
        


        

    
