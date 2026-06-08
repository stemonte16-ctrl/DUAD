"""characters"""

def return_characters(text, character):
    
    count_characters = 0
    
    for letter in text:
        if letter == character:
            count_characters += 1
    return count_characters


print(return_characters("Hello", "l"))