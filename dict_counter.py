this_dict = {"a":1, "b":2, "c":3}

string = []

for key in this_dict:
    string.append(key * this_dict[key])
print(str(string).strip("[]"))



def dict_maker(a_string):
    empty_dict = {}
    for letter in a_string:
        if  letter in empty_dict:
            empty_dict[letter] += 1
        else:
            empty_dict[letter] = 1
    print(empty_dict)

dict_maker("aavvvc")

def anagram(string1, string2):
    
    if len(string1) != len(string2):
        print("This works!")
        return False
    string1sort = sorted(string1.upper())
    string2sort = sorted(string2.upper())
    if string1sort == string2sort:
        print("Got it!")
        return True
    else:
        print("Yep!")
        return False

anagram("listen", "SIoENT")