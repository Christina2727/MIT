#Christina Roberts
#conditional_examples.py
#lecture 2 assignment 2

#Boolean math

#Examples of if statements
#general format
# if <condition is True>:
#     <code to execute if condition is True>

"""if 9 > 5:
    print( "Yes, 9 is greater than 5")

if 9 != 5:
    print("Yes, 9 is NOT equat to 5")

#An example of an if/else statemet
#General format:
#if <condition is True>:
#   <code to execute if condition is True>
#else:
#   <code to execute if condition is False>"""

if 9 < 5:
   print( "Yes, 9 is less than 5")
else:
   print("No, 9 is NOT less than 5")

# An example using "not" and "and" keywords
if not (10 ==4 ) and 9 > 5:
    #basically the line above says if 10 is not equal to 4 and 9 is not greater
    #than 5, becuase in the begining it says if NOT
    print("Yay, basic math competency achieved!")
else:
    print(":(")

#Traffic light example
light_color = input("What color is the traffic light? ")
light_color = light_color.upper()
print(light_color)
if light_color == "red":
    print("you should stop")
elif light_color == "yellow":
    print("Slow Down !!")
elif light_color == "green":
    print("Go aheadh!" )
else :
    print("What country are you in?")

