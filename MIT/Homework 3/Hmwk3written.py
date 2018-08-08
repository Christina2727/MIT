"""Exercise 3.9 – Mystery Program
Ben next turned in the following uncommented code to the 6.189 LAs. Help us
figure out what it does!"""

print("Think of a number between 1 and 100, but don’t tell me what you choose.")
min_n = 1
max_n = 100
right_answer = False

while not right_answer:
    mid_n = (max_n + min_n + 1)/2
    answer = input("Is it " + str(mid_n) + "? ")
    if answer[0] == "y":
        right_answer = True
    elif answer.startswith("higher"):
        min_n = mid_n + 1
    elif answer.startswith("lower"):
        max_n = mid_n - 1
    else:
        print("Sorry, I don’t understand your answer.")

print ("Woohoo! I got it!")


"""1. The while loop exits when the variable right answer is True. What will
cause right answer to be true?"""
#if the character y is in index place 0. If player typed "y"


"""2. How many times will the program print out ’Woohoo! I got it!’?"""
# 1

"""3. What are we using the variable answer for?"""
#to see if the players input tells us if 1. we got the answer right (y)
#2. players number is (higher) 3. players number is (lower) and we need
# to adjust computers guess accordingly


"""4. The program makes a guess in line 8. What user responses will be
understood by the program after it makes its guess?"""
#y, higher, lower

"""5. If the program gets the response ’higher’, what does that tell it
about its guess?""" #computer needs to guess a higher number


"""6. What are the variables min n, max n and mid n used for?
This is an example of binary search, a simple but important algorithm in
computer science. If you’re curious, or confused, read the Wikipedia
article on binary search to find out more and get a good explanation of what’s
going on here."""
#minimum number that can be guessed
#maximum number that can be guessed
#mid = (min + max +1 )/2 --- i thought that would just be (100+1+1)/2
#and then it would increase or decrease by one with each computer guess.
#instead it either divides itself by 2 (like 51 to 26) or
#it adds 50% of its value back (like 13.5  to 20.25
# and im not sure how that happens with the math thats written in the code
