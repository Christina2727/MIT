"""3.11 – Understanding Objects"""

"""1. Write a class called Address that has two attributes: number and street
name. Make sure you have an init method that initializes the object
appropriately."""
class Adress():
    def __init__(self, number, streetname):
        self.number = number
        self.streetname = streetname
    
"""2. Consider the following code:"""

class Clock:
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = "6:30"
        print(self.time)
clock = Clock("5:30")
clock.print_time()

"""(a) What does the code print out? If you aren’t sure, create a Python file
and run it."""
# 5:30
#we set parameter for class Clock to 5:30 so that over rules the
#local varibale in print_time function

"""(b) Is that what you expected? Why?"""
#no

"""3. Consider the following code:"""
class Clock:
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)
clock = Clock("5:30")
clock.print_time("10:30")

"""(a) What does the code print out? If you aren’t sure, create a
Python file and run it."""
#10:30

"""(b) What does this tell you about giving parameters the same name as
object attributes?"""
#dont do it. time in print_time (parameter) was named the same as time
#  in the __init__ method which was an attribute 

"""4. Consider the following code:"""
class Clock:
    def __init__(self, time):  #ATTRIBUTE TIME
        self.time = time
    def print_time(self):
        print(self.time)
boston_clock = Clock("5:30") #1
paris_clock = boston_clock    #2 paris_clock = Clock("5:30")
paris_clock.time = "10:30"   #3 changes the attribute in class Clock to 10:30
boston_clock.print_time()     #4 prints the changes arttribute of 10:30


"""(a) What does the code print out? If you aren’t sure, create a
Python file and run it."""

#10:30
"""(b) Why does it print what it does? (Are boston clock and paris clock different objects? Why or why
not?)"""
#commented in code to explain why
