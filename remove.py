n = [1,3,6,6,7,10,10,1]
s=[]

for item in n:
      if item not in s:
          s.append(item)
          
print(s)

dupNames ={"a","b","c","b","c"}
print(list(set(dupNames)))
dubset=set(dupNames)
print(dubset)
newlist=list(dubset)
print(newlist)








    