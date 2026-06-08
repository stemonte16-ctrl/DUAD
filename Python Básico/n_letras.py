"""n_letters"""

def more_of_n_letters(list_1, n):
    new_n = []
    
    for word in list_1:
        if len(word) > n:
            new_n.append(word)
    
    return new_n


print(more_of_n_letters(["sol", "sal", "comer", "dormir", "Dios"], 3))