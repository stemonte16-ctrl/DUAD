"""iterables"""
my_list = []

for words in range(5):
    names = input("ENTER 5 WORDS: ")
    my_list.append(names)

new_list = []

for words in my_list:
    if len(words) > 4:
        new_list.append(words)

print(new_list)
