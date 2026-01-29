first_name= 'Javi'
last_name= 'Martinez'
full_name= 'Javi Martinez'
country= 'Mexico'
city= 'Monterrey'
age= '300'
year= '2026'
is_married= False
is_true= True
is_light= 10j

is_morning, is_afternoon, is_night = 'true','false','No'


print(type(first_name))
print(len(first_name))
print(type(last_name))
print(len(last_name))
print(len(first_name)-len(last_name))
num_one= 5
num_two= 4
print(num_one + num_two)
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(is_morning, is_afternoon, is_night)
product = num_two * num_one
print(product) 

product_division = num_two / num_one
print(product_division)

remainder = num_two % num_one
print(remainder)

power= num_one ** num_two
print(power)

radius = int(input())
pi = 3.14159
area_of_circle = ( radius ** 2 ) * pi
print('area of circle :', area_of_circle)

circum_of_circle = (2*pi*radius)
print('circumference of circle: ',circum_of_circle)

first_name = input()
print(first_name)

help('keywords')