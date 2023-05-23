#task1
import datetime
a=datetime.datetime.now()
class clock():
    def __init__(self):
        self.hour=hour
        self.minute=minute
        self.second=second
    def display_clock(self):
        return f"{self.hour}:{self.minute}:{self.second}"

class calendar():
    def __init__(self,month,day):
        self.month=month
        self.day=day
    def display_calendar(self):
        return f"{self.month}/{self.day}"
    
class calendarclock(clock,calendar):
        def __init__(self,hour,minute,second,month,day):
          #  super().__init__(self,hour,minute,second,month,day)
            self.hour=hour
            self.minute=minute
            self.second=second
            self.month=month
            self.day=day

calendarclock1=calendarclock(a.hour,a.minute,a.second,a.month,a.day)
print(calendarclock1.display_clock())
print(calendarclock1.display_calendar())

#task2
import numpy as np
class Collinear():
     def __init__(self,x,y):
          self.x=x
          self.y=y
p1=Collinear(0,3)
p2=Collinear(3,4)
p3=Collinear(2,4)          
a = np.array([[p1.x,p1.y,1], [p2.x,p2.y,1],[p3.x,p3.y,1]]) 
if (np.linalg.det(a))==0:
     print("Collinear")
else:
     print("Non-Collinear")  

#task3

class Employee():
  def __init__(self):
    pass
  def inputData(self):
    self.id = input("Enter Employee id ")

  def printData(self):
    print("Employee id is: ",self.id)

class Manager(Employee):
  def __init__(self):
    pass
  def inputData(self):
    super().inputData()
    self.dep_id = input("Enter Department")

  def printData(self):
    super().printData()
    print("Department: ",self.dep_id)

class Project(Manager):
  def __init(self):
    pass
  def inputData(self):
    super().inputData()
    self.proj = input("project?")

  def printData(self):
    super().printData()
    print("Project: ",self.proj)

obj = Project()
obj.inputData()
obj.printData()