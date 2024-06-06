# Question 1:
"""li=[1,2,3,4,5,6,7,8,9,10]
li=[x for x in li if x%2==0]
print(li)"""

# Question 4:
"""string_list=['apple','banana','cherry','Date']
short_list=sorted(string_list,key=lambda x:len(x))
print(short_list)"""
# Question 5:
class Vehicle():
    def drive(self):
          print("Driving a Vehicle")
class Car(Vehicle):
         def drive(self):
            print("Car is started.Let's drive.")
class Truck(Vehicle):
         def drive(self):
            print("Truck is started.Let's drive.")
class Motorcycle(Vehicle):
         def drive(self):
            print("Motorcycle is started.Let's drive.")

Vehicle=Vehicle()
Vehicle.drive()
Car=Car()
Car.drive()
Truck=Truck()
Truck.drive()
Motorcycle=Motorcycle()
Motorcycle.drive()


