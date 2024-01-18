def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def First_Two_Letters(s):
    for letter in s[0:2]:
        if letter.isalpha(): 
            return True
        else:
            return False

def length_Checker(s):
    if 2 <= len(s) <= 6:
        return True
    else: 
        return False
    
def num_Checker(s):
    boolee = True
    num_location = 0
    for character in s: 
        if character.isdigit(): 
            num_location = s.index(character)
            break
    
    sliced_word = s[num_location: ]

    if num_location != 0: 
        if (sliced_word.isdigit() and (sliced_word[0] != "0")):
            boolee = True
        else:
            boolee = False
    
    return boolee

def punct_checker(s):
    boolee = True
    for character in s: 
        if character.isalpha() or character.isdigit():
            boolee = True
        else: 
            boolee = False
    return boolee



def is_valid(s):
    if First_Two_Letters(s):
        if length_Checker(s):
            if punct_checker(s): 
                if num_Checker(s):
                    return True
                else: 
                    return False
if __name__ == "__main__":
    main()