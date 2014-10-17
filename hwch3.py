# HW CH 3 EXERCISES

#1a) 7.4    b) 5.0    c)8   d) error because sqrt requires import function
#e)11   f)27

#3a) 0,1,2,3,4      b) 3,4,5,6,7,8,9        c) 4,7,10
#d) 15,13,11,9,7    e) nothing

#4a) 14,9,16,25,36,49,64,81,100     b) error
#c) 012,212,412,612,812, done       d) 1,2,3,4,5,6,7,8,9,10,385

#6a)-4     b)2     c)-4    d)-2     e)3

from math import *

def sphere():
    r=eval(input("Enter the radius of the sphere: "))
    V=4/3*pi*r**3
    A=4*pi*r**2
    print("The volume of the sphere is",int(V),"and the surface area is,",int(A),end=".\n\n")
sphere()

def coffee():
    p=eval(input("Enter how many pounds of coffee you want to order: "))
    x=10.50*p
    y=.86*p+1.50
    z=x+y
    print("The cost of the order is $",end="")
    print(float(z),end=".\n\n")
coffee()

def slope():
    x1,y1=eval(input("Enter the coordinates of the first point separated by a comma: "))
    x2,y2=eval(input("Enter the coordinates of the second point separated by a comma: "))
    m=(y2-y1)/(x2-x1)
    print("The slope is",m,end=",")
slope()




    
