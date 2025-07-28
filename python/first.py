'''print('hello world')
print("abc")
print("he said,\"he lost\"")
print("he :\\")  #he
a={"2":"l"}
print(type(a))
a=[9,9,0]
print(a[2])
p=[7,9,0]
p[0]="l"
print(p)
print()
a=int(input("enter number to be entered :"))
if a%2 ==0:
    print("even")
else :
    print("jhjsjx") 
a=6
a-=5
print(a)
b=89
print("child"if(b<100)else "elder")
print("even"if(b%2==0)else "odd")
if 5==5: 
    pass
print() 
for i in range(1,10) :
    if i == 4:
        print("uh")
    print(i+9)
a=[1,2,33,4,56,6,43]
for i in a :
    print(i)
k=("ggvbghfhgfuyghgnkijbhg","gh","j","hg","jh")
k[4]=="t"
print(i)
print(i)
print(k)
s={5,97,79,8,97}
d={445,5,97,76,78,4,87}
print(s.intersection(d))
print(s.union(d))
print(s.difference(d)) 

#FUNCTIONS
def kl():
    a=input("enter a word:")
    print(a,"world")
kl()
def ab(a,b):
    return a+b
def cf(a,b):
    return a-b
a=int(input("enter a number"))
b=int(input("enter a number"))
t=ab(a,b)
j=cf(a,b)
print(t,"\n",j)
#global and local scope

a=39
def add():
    a=98    #global used for not allowing global value 
    print(a)
add()
print(a)  
 
 #recursion

def ab(n):
    if n==1:
        return 1
    return n*ab(n-1)
print(ab(2))

def ab(n):
    if n==0:
        return 1
    return n*ab(n-1)
result=ab(4)
print(result) 


# class&opps
class car:
    def __init__(self,wheels,mileage,airbags,carname,):
        print("this is constructor")  #prints when the object is created
        self.__wheels=wheels
        self.airbags=airbags
        self.mileage=mileage
        self.carname=carname
    def __del__(self):
        print("this is a destructor",self)
    def __str__(self):
        return(self.carname)
    def ab(self,speed):
        print("car",speed)
    def bt(self):
        print("nike")
    #getter
    def get_wheels(self):
        print("no of wheels:",self.__wheels)
car_1=car(4,65,4,"swift")
#print(car_1)
print(car_1.mileage,car_1.get_wheels(),car_1.airbags)
#car__2=car(65,89,8,"innova")
#print(car_2.mileage,car_2.__wheels,car_2.airbags)
car_1.wheel=25
print(car_1.wheel)
print(car_1.get_wheels())
    

    #problem
class mobile : 
    def __init__(self,brand,model,price):
        self.__brand=brand
        self.__model=model
        self.__price=price
        print("this is an constructor",self)

    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price
    def __str__(self):
        return f"mobile({self.__brand},{self.__model})"
    
mobile_1=mobile("moto","edge 50",20000)
print(mobile_1.get_brand())
print(mobile_1.get_model())
print(mobile_1.get_price())

mobile_2=mobile("oppo","a54",20000)
print(mobile_2.get_brand())
print(mobile_2.get_model())
print(mobile_2.get_price()) 

#encaptulation problem

class student:
    def __init__(self,name,roll,grade):
        self.__name=name
        self.__roll=roll
        self.__grade=grade
    def get_name(self):
        return self.__name
    def get_roll(self):
        return self.__roll
    def get_grade(self):
        return self.__grade
    def __str__ (self):
        return (self.__name)
    def set_name(self,name):
        self.__name=name
student_1=student("dk",6,12)
print(student_1)
student_2=student("vk",16,12)
student_1.set_name("kk")
student_2.set_name("abd")
print([student_2.get_name(),student_2.get_roll(),student_2.get_grade()])
print([student_1.get_name(),student_1.get_roll(),student_1.get_grade()])


#INHERITANCE
#single class
class vehicle:  #parent class
    wheels=3
    def moveforward(self):
        print("vehicle moving")

class car(vehicle): #inheritance child class
    airbags=7
car_2=car()
print(car_2.wheels)
car_2.moveforward()

#hierarchical inheritance(double class)
#class bike(vehicle):
  #  gear=5


class maruthi(car):        #multilevel inheritance
    mileage=25
car_1=maruthi()
print(car_1.wheels)
print(car_1.airbags)
print(car_1.mileage)

#multiple inheritance 2parent class + 1child class

class sport:
    game="cricket"
class gayle(sport):
    highest="six"
    name="boss"
class vk(gayle):
    role="rhb"
    name="king"
class abd(gayle):
    name="Mr.360"
class dk(vk,abd):
    order="opener"
dk=dk()
print(dk.name)
print(dk.order)
print(dk.role)
print(dk.highest) 

#polymorphism
class car:
    def sum(self):
       print("animal speaks")
class bike(car):
    def sum(self):
        print("dog barks")
class vehicle(car):
    def sum(self):
        print("cat meows")
fuel=[car(),bike(),vehicle()]
for i in fuel:
    i.sum() 

    #abstraction -------->simplfy

from abc import ABC,abstractmethod
class car(ABC):
    a=0
    @abstractmethod   #@ using decorators
    def movebackward():
        pass
    @abstractmethod
    def movebackward():
        print("hiu")
    @abstractmethod
    def fm(self):
        pass
class swift (car):
    @staticmethod
    def moveforward(): #static method dosent need arugument
        print("swift is moving forward")
    @staticmethod
    def movebackward():
        speed=30
        acceleration=speed*10
        print("swift is backward",acceleration)
    def fm(self):
        print("swift is fm")
class innova (car):
    def moveforward(self):
        print("innova is moving forward")
    def movebackward(self):
        print("innova is backward")
    def fm(self):
        print("innova is fm")
swift=swift()
#swift.movebackward()
swift.moveforward()
car.movebackward()
car.a=989
print(car.a)'''


#static method

class car:
    wheels=4
    def __init__(self,brand):
        self.brand=brand
car_1=car("toyota")
car_2=car("honda")
print(car_1.wheels)
print(car_2.wheels)
