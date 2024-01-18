camel_phrase = input("Camel Case: ")
new_string = ""

first_character = True

for c in camel_phrase:
    # Check if the character is uppercase
    if c.isupper():
        # Avoid adding underscore before the first character
        if not first_character:
            new_string += '_'
        first_character = False
    else:
        first_character = False
    
    new_string += c


# Convert the new string to lower case

print(new_string.lower(), end="")

