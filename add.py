n=[8,9,3,1,2,0,5,0]
m=[]
for item in n:
  m.append(item)
print(m)
m.append(55)
print(m)
print(n)

zero=[]
num=[]
for item in n:
   if item !=0:
      num.append(item)
   else:
      print(item)
      zero.append(item)

print(num)
print(zero)
      
     