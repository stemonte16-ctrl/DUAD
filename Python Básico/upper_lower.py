"""upper and lower"""


def total_upper_cases_lower_cases(text):
    
    counter_upper = 0
    counter_lower = 0
    
    for letter in text:
        if letter.isupper():
            counter_upper += 1
        elif letter.islower():
            counter_lower += 1
    
    return counter_upper, counter_lower

upper, lower = total_upper_cases_lower_cases("I love Nación Sushi")
print(f"There are {upper} upper cases and {lower} lower cases")