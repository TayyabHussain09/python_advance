import string
from tkinter import Y


x=10
y=10.2
z="hello ! tayyab"
#below is called implicit type conversion
x=x+y
print(x,"type of x is:",type(x))

#explicit type conversion
age=input("what is your age? ")
#age=int(age)
print(age, type(int(age)))  #see you can write multiple functions like this and can change the class type within the line
