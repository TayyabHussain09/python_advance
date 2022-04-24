from ctypes.wintypes import MSG
#getting the messages detail

msg='hey tayyab hussain welcome to my jungle bro'
print(msg.lower())
print(msg.upper())
print(msg.swapcase())

#getting some mixed input details

animal = input("what is your fav animal?")
print(animal)
animal="markhor"
print(animal)
building = input("what is your fav building")
print(building)
building="Burg Al Khalifa"
print(building)
color = input("what is your fav color")
print(color)
color = "black"
print(color)
print("what the fuck you want to print")
print("The "+color+" "+animal+" ran up the "+building)

#getting mixed input names etc

firstName = input("what is your first name?")
lastName = input("what is your last name?")
print(firstName)
print(lastName)
firstName="tayyab"
lastName="hussain"
print("Hello " + "Tayyab" " " + "hussain")
name=input("what is your name")
print(name)
print('hello, ' + name)

#experiment with the finding tricks of python.
msg = "vvannoto genoq"
print(msg.find('genoq'))
print(msg.count('v'))
print(msg.capitalize())
print(msg.replace('vvannoto','ghanta'))
