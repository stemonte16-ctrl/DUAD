"""how many vowels are there"""

def how_many_vowels(text):
    counter = 0
    
    for letter in text.lower():
        if letter in "aeiou":
            counter += 1
    
    return counter

print(how_many_vowels("Montenegro"))