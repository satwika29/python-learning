class Myclass:
    x=5
p1= Myclass()
print(p1.x)


class Student:
    def __init__(self):
       print("hello world")
    def emp(self):
       print("hello world")
    def abc(self):
       print("Hello world")
p1=Student()
p1.emp()
p1.abc()





class Company:
    def __init__(self):
        print("Class started")
    def hi(self,msg):
        print(msg)
c = Company()
#c.hi()

c1 = Company()

c2 = Company()
c.hi("hi")
c1.hi("hi")

c2.hi('hi')


class Compiny:
     def __init__(self,name,age):
         print("class strated")
         self.name=name
         self.age=age
     def student(self):
         print("student")
p1=Compiny("satwika",21)
p2=Compiny("nandu",23)
p1.student()




