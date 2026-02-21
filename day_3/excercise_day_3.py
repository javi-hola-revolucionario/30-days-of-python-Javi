age = 27
height = 1.76
complicated = 10j

#script that prompts the user to enter base and height of a traingle and calculate an area of this triangle (0.5 * b* n)

base = float(input('write the base: '))
height = float(input('write the height: '))

area_of_traingle = base * height * 0.5

print('The area of traingle is: ', area_of_traingle )

# write a script that prompts the user to enter side a, side b, and a side c of the triangle. Claculate the perimtere of the triangle 

a = int(input('enter side a: '))
b = int(input('enter side b: '))
c = int(input('enter side c: '))
perimeter = a + b + c
print('perimeter of triangle is: ', perimeter)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y=mx+b

m = 2
b = -2
x = -b / m
print('The slope is: ',m)
print('The b value is: ',b)
print('x intercept is: ', x)
print('end of excercise')

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

y2 = 10
y1 = 2
x2 = 6
x1 = 2

m2 = (y2 - y1) / (x2 - x1)

print('The slope that was calculated from two points is, ',m2)

print('-------------The euclidean distance is -----------------')

d = ((y2 - y1)^2 + (x2 - x1)^2)*1/2
print('Based on the calculations its: ', d)
#
print('lenght of the word python is:',len('python'))

# nos saltamos algunos ejercicios 


#Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

n = 1

for n in range(1,6):
    print(n)
    #, n**0, n**1, n**2, n**3)