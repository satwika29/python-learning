name="satwika"
print(name)

list =["satwika","nandu","ashu"]
print(list)
for item in list:
    print (item)

my_Dict ={"name":"satwika", "id":"sattu@gmail.com"}
print(my_Dict)
#print(my_Dict.get(2))
print(my_Dict.keys())
print(my_Dict.values())

set={"kavya","hari"}
print(set)
for item in set:
    print(set)
     

'''
tuple_1=("a","b","c")
print(tuple_1)
tuple2= list(tuple_1)
print(list)'''



def function():
    stu = {"name":"abcd","id":1}
    student = [{"name":"hari","id":"hari@gmail.com"},{"name":"rabiya","id":"rabiya@gmail.com"}]
    for item in student:
        print('name',item['name'],'id',item['id'])
function()


list =[1,2,3,4,5,6]
for item in list:
 print(item)
 if item % 2 == 0:
    print ( "even")
else:
    print("add",item)