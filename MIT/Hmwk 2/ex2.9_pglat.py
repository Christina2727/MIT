Exercise 2.9 – Pig Latin
Write a function pig latin that takes in a single word, then converts the word
to Pig Latin. To review, Pig Latin
takes the first letter of a word, puts it at the end, and
appends “ay”. The only exception is if the first letter is a
vowel, in which case we keep it as it is and append “hay” to the end.
E.g. “boot” → “ootbay”, and “image” → “imagehay”.
It will be useful to define a list at the top of your code file called
VOWELS. This way, you can check if a letter x is a
vowel with the expression x in VOWELS. Remember - to get a word except for
the first letter, you can use word[1:]. Be sure to look at the first optional
problem for ways to improve on your Pig Latin converter.
