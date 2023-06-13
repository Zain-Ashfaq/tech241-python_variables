# get user name, age, dob, address and print it back to them

name = input("What is your name?\n" )
age = int(input("What is your age?\n" ))
dob = input("What is your date of birth?\n" )
address = input("What is your address?\n" )

#print("your name is",name,"\nyour age is",age,"\nyour date of birth is",dob, "\nyour address is", address)

print(f"your name is {name}, your age is {int(age)}, your dob is {dob}, your address is {address}")
