# 6.189 Lecture 1
# raw_input_example.py


name = input("What is your name? ")
city = input("What city do you live in? ")
state = input("What state is that in? ")

"""print("Hello there! It is so great to meet you")
print(name)
print("from")
print(city)
print(state)"""

print("Hello there! It is so great to meet you ")
print(name, "from", city, state)
print(" ")
age = int(input("Pardon my rudeness, but how old are you?"))

print("Wow, you look like you could be" , int(age -(0.15*age)), "!!" )

