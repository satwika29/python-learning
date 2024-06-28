def mytuple (a,b,k):
  c=a+b+k
  print(c)
mytuple(10,20,30)

tuple=(20,30, 40)
def addition(tuple):
  a,b,c= tuple
  num=a+b+c
  print(num)
addition(tuple)

thislist=[20,30, 40]
addition(thislist)

#python program to calculate Simple intrest

 p=100
t=20
r=3

def interest(p,t,r):
  Si=(p*t*r)/100
  print(Si)
interest(p,t,r)

class Person:              

          
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



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



                 







 