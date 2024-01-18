def main():
    first_phrase = (input("Input: "))
    print("Output:", shorten(first_phrase))

def shorten(first_phrase):
    new_Phrase = ""
    vowels = "aeiouAEIOU"
    for letter in first_phrase:
        if letter not in vowels:
            new_Phrase += letter
    return(new_Phrase)

if __name__ == "__main__":
    main()