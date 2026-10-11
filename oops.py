'''class grandfather ():
    def land(self):
        print("grandfather's properties")
g=grandfather()
g.land()

class father(grandfather):
    def house(self):
        print("father's properties",father)
f=father()
f.house()

class mother():
    def gold(self):
        print("mother's properties")
m=mother()
m.gold()

class daughter(grandfather,mother):
    def scooty(self):
        print("daughter's properties",daughter)
d=daughter()
d.scooty()
d.land()
d.gold()'''

'''class son(father):
    def car(self):
        print("son's properties",son)
s=son()
s.car()
s.land()
s.house()'''

'''class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=student("mikey",77)
print(s1.name)
print(s1.marks)'''

'''class car():
    def start(self):
        print("start")
c=car()
c.start()'''

'''class laptop():
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
l=laptop("HP",70000)
print(l.brand)
print(l.price)'''

'''class book():
    def __init__(self,author,title):
        self.author=author
        self.title=title
b=book("guido van russo","python programming")
print(b.author)
print(b.title)'''

'''class mobile():
    def call(self):
        print("make a call")
m=mobile()
m.call()'''

'''class animal():
    def eat(self):
        print("animals eating")
class dog():
    def call(self):
        print("call the dog by its name")
a=animal()
a.eat()
d=dog()
d.call()'''

'''class vehicle():
    def start(self):
        print("start the vehicle")
class bike(vehicle):
    def start(self):
        super().start()
        print("start the bike")
b=bike()
b.start()'''

'''class person():
    def __init__(self,name):
        self.name=name
class student():
    def __init__(self,name):
        self.name=name
p=person("deva")
print(p.name)
s=student("manoj")
print(s.name)'''

'''import math
class shape():
    def area(self):
        print("area of the shape")

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
c=circle(7)
print("radius of the circle",c.area())'''

'''class employee():
    def salary(self):
        print("employee salary")
class manager():
    def __init__(self,salary):
        self.salary=salary
e=employee()
e.salary()
m=manager(120000)
print(m.salary)'''

'''class father():
    def land(self):
        print("father's properties")
class mother():
    def gold(self):
        print("mother's properties")
class child(father,mother):
    def bike(self):
        print("child's properties")
c=child()
c.bike()
c.land()
c.gold()'''

'''class schoolmember():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"name.{self.name},age.{self.age}")
class teacher(schoolmember):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject=subject

    def info(self):
        super().info()
        print(f"role:teacher,subject:{self.subject}")
class student(schoolmember):
    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.marks=marks

    def info(self):
        super().info()
        print(f"role:student,marks:{self.marks}")
t1=teacher("Rama",30,"english")
s1=student("Manoj",23,90)
t1.info()
print("-------------->")
s1.info()'''

'''class phone():
    def __init__(self,price,camera):
        self.price=price
        self.camera=camera
    def info(self):
        print(f"price:{self.price},camera:{self.camera}")
class smartphone(phone):
    def __init__(self, price, camera,advantages,brand):
        super().__init__(price, camera)
        self.advantages=advantages
        self.brand=brand

    def info(self):
        super().info()
        print(f"brand:iphone,advantages:high performance access to everything through smartphone")
ph=phone(1000,2)
sp=smartphone(150000,50,'iphone',"high performance access to everything through smartphone")
ph.info()
print("------------>")
sp.info()'''


'''class grandparent():
    def land(self):
        print("grandparent's properties")
class parent(grandparent):
    def house(self):
        print("parent's properties")
class child(parent):
    def bike(self):
        print("child's properties")
c=child()
c.bike()
c.house()
c.land()'''

'''class vehicle():
    def bike(self):
        print("bike runs by petrol or diesel")
class car(vehicle):
    def car(self):
        print("car runs by petrol or diesel")
class electriccar(car):
    def eleccar(self):
        print("electric car runs by electric charge")
el=electriccar()
el.bike()
el.car()
el.eleccar()'''

class animal():
    def dog(self):
        print("dog barks")
class cat(animal):
    def cat(self):
        print("cat meows")
c=cat()
c.cat()
c.dog()




    


