#ex 2.10

"""1. Write a list comprehension that prints a list of the cubes of the numbers
    1 through 10."""

cubes = [y**3 for y in range(1,11)]
print(cubes)


"""2. Write a list comprehension that prints out the possible results of two
    coin flips (one result would be ’ht’).(Hint - how many results should
    there be?)"""

new_list = [x+y for x in["h", "t"] for y in ["h", "t"]]
print(new_list)

"""3. Write a function that takes in a string and uses a list comprehension to
    return all the vowels in the string."""

#def vowel(string): #y and w are sometimes vowels
#    for i in string:
#        if "a" "e" "i" "o" "u" "y" "w" in string: #broken 
"""TypeError: 'in <string>' requires string as left operand, not list"""        
#            return[x for x in string if x in vowels]
        
#        else:
#           print("no vowels")

#vowel("Charlie")
#WHAT WOULD I CHANGE TO MAKE THIS TOP VERSION WORK IF EVEN THOUGH I KNOW ITS
#LONGER

def vowels(string):
    vowels = ["a", "e", "i", "o", "u", "y", "w"]
    return[x for x in string if x in vowels]

print(vowels("charlie"))


"""4. Run this list comprehension in your prompt:
    [x+y for x in [10,20,30] for y in [1,2,3]]
    Figure out what is going on here, and write a nested for loop that gives you
    the same result. Make sure what
    is going on makes sense to you!"""

    #will give sum ofdifferent combinations of addition problems like
    #10+1 "11" 10+2 "12" 30+1 "31" etc


simple_adding = [x+y for x in [10,20,30] for y in [1,2,3]]
print(simple_adding)
