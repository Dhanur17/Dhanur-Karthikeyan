print('hello world')
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
    def __init__(self,wheels,mileage,airbags,carname):
        print("this is constructor")  #prints when the object is created
        self.wheels=wheels
        self.airbags=airbags
        self.mileage=mileage
        self.carname=carname
    def __del__(self):
        print("this is a destructor",self)
    def ab(self,speed):
        print("car",speed)
    def bt(self):
        print("nike")
    def __str__(self):
        return(self.carname)
car_1=car(78,98,78,"swift")
print(car_1)
print(car_1.wheels)
car__2=car(65,89,8,"innova")
print(car__2)
print(car__2.wheels)
     

    #problem
class mobile : 
    def __init__(self,brand,model,price):
        print("this is an constructor",self)
        self.brand=brand
        self.model=model
        self.price=price
    
mobile_1=mobile("moto","edge 50",20000)
print(mobile_1.brand)
print(mobile_1.model)
print(mobile_1.price)

mobile_2=mobile("oppo","a54",20000)
print(mobile_2.brand)
print(mobile_2.model)
print(mobile_2.price)

print("**************************COMPLETED*******************")

