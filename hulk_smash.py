a_dict = {"Hulk":"Unsmashed", "Thor":"Unsmashed", "Iron Man":"Smashed", "Spider-man":"Smashed by Sony"}
def hulk_smash(a_dict):
    for key in a_dict:
        dict_full = len(a_dict)
        if len(a_dict) > dict_full/2:
            a_dict.pop(key)
        else:
            break
    return a_dict
print(hulk_smash(a_dict))
print(len(a_dict))
