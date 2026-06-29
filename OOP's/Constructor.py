class demo:
    def __init__(self):
        print("Default constructor called")
    
# object name
obj=demo()

#1. class variable.

class demo1:
    #classvariable
    ins_name="Linkcode" 

#2.instance variable

print(demo1.ins_name)
obj1=demo1()
print(obj1.ins_name)



# instance variable ------>create manually

class demo2:
    def __init__(self):# self is used to represent currnet member of class.

        self.name="Nikita"
        self.age=21

obj2=demo2()
print("Name:",obj2.name)
print("Age:",obj2.age)

class mobile:
    def __init__(self,Uname,Ubrand,Ucolor,Uprice):
        self.name=Uname
        self.brand=Ubrand
        self.color=Ucolor
        self.price=Uprice

obj=mobile("iphone14","Apple","BLack","120000")
print(obj.name,obj.brand,obj.color,obj.price)

obj1=mobile("iphone14","Apple","Pink","40000")
print(obj1.name,obj1.brand,obj1.color,obj1.price)


#Store obejct inside the loop 

x=[obj,obj1]
for i in x:
    print(i.name)

#Example of constructor with multipke objects and instance variable 
#1.
class Brand:
    def __init__(self,name,model,wheels,price,quantity):
        self.name=name
        self.model=model
        self.wheels=wheels
        self.price=price
        self.quantity=quantity
obj1=Brand("Scorpio","s2",4,1200000,1)
obj2=Brand("Shine","s5",2,700000,5)
obj3=Brand("thar","s3",4,2000000,5)
obj4=Brand("Honda","s7",2,1400000,2)
obj5=Brand("Activa","s1",4,200000,5)

x=[obj1,obj3,obj4,obj5]
total=0
for i in x:
    print(i.name,i.model,i.wheels,i.price,i.quantity)
    print("======================================")
    total +=i.price*i.quantity
print("Total value:",total)
print("==================================")
for i in x:
    if i.quantity<5 and i.quantity<10:
        print(i.name,i.quantity)

