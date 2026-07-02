#Day 5 Lists

# There are four collection of data types in Python: 

# List, is a collection which is ordered and changeable. Allows duplicate members.

# Tuple: is a collection which is ordered and unchangeable or unmodifiable (immutable). Allow duplicate members.

# Set: is a collection which is unordered, un-indexed and unmodifiable, but 
# we can add new items to the set. Duplicate memebers are not allowed. 

# Dictionary: is a collection which is unordered, changeable (modifiable) and indexed. No duplicate members.

# syntax for list

lst = list() # creates an empty list
lst = [] # this is an empty list, no item in the list

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies


print('I hate fruits: ', fruits)

# A list can have items of different data types

lst =['Javier',29, True, {'pais': 'Mexico', 'cuidad': 'Monterrey'}]
print(lst)

print(len(lst))
# We can access a list through its index. We can also use the negative for starting from the end.

print(fruits[0], fruits[len(fruits)//2], fruits[-1]) 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

sort_ages = sorted(ages)
print(sort_ages)