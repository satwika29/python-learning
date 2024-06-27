dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

print(dict1)
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items())
print(dict2.keys())
print(dict2.values())
print(dict2.pop(4))
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3:"sacla"})
print(dict2)

#all() checks if all values in the dictionary evaluate to True.
#any() checks if any value in the dictionary evaluates to True.
#cmp() (no longer available in Python 3) used to compare two dictionaries.
#sorted() returns a new sorted list of keys in the dictionary.



my_dict = {'A': 10, 'B': 20, 'C': 0}
print(all(my_dict.values()))  #False (0 evaluates to False)
print(any(my_dict.values())) # True (at least one value is True)
print(sorted(my_dict)) #print(sorted(my_dict)) 


Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

#Add values to dictionary Using two lists of the same length

roll_no = [10, 20, 30, 40, 50]
names = ['Ramesh', 'Mahesh', 'Kamlesh', 
         'Suresh', 'Dinesh']
 
students = dict(zip(roll_no, names))
print(students)

#converting list to dictionary

vegetables = ['Carrot', 'Raddish', 
              'Brinjal', 'Potato']
 
veg_dict = dict(enumerate(vegetables))
print(veg_dict)