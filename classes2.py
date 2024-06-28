class Compiny:
     def __init__(self,name,age):
         print("class strated")
         self.name=name
         self.age=age
     def student(self):
         print("student")
p1=Compiny("satwika",21)
#p2=Compiny("nandu",23)
p1.student()


class Calculator:
    def __init__(self):
     pass
    def add(self,a,b):
      print(a+b)
    def sub(self,a,b):
      print(a-b)
c=Calculator()
c.add(10,20)
c.sub(10,20)


class Cal:
    name = 'hi'
    def __init__(self):
        pass
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
c = Cal()
c.add(10,20)
c.sub(20,10)