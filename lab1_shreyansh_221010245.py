#program 1
class Car():
    def __init__(self,make,model,color,year,transmission,displacement,engine):
        self.make=make
        self.model=model
        self.color=color
        self.year=year
        self.transmission=transmission
        self.displacement=displacement
        self.engine=engine
car1= Car("volvo","V60","red",2018,"Automatic",2.4,"V6")
car2= Car("Cadillac","Excalade","black",2022,"Automatic",5,"DuramaxV8")
print(car1.__dict__)
print(car2.__dict__)

#program 2
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_Details(self):
        print("person name : "+self.name,end=" ")
        print(",person age : "+str(self.age))    
person1 =person("Fof",19)          
person2 =person("Freeyanshu",20)    
person1.print_Details()
person2.print_Details() 

#program 3
class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth
        return area
    def perimeter(self):
        perimeter= (self.length+self.breadth)*2
        return perimeter
rectangle1 = rectangle(10,12)    
print("area of rectangle 1 is "+str(rectangle1.area())+" unit^2")
print("perimeter of rectangle 1 is "+str(rectangle1.perimeter())+" unit")