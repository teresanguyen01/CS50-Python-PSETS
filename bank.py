def main():
    greetings = input("Greeting: ")
    values = value(greetings)
    print(f"${values}")

def value(greetings):
    greetings.strip().lower()
    if (greetings[0:5] == "hello"):
        return(0)
    elif(greetings[0:1] == "h"):
        return(20)
    else:
        return(100)
    
if __name__ == "__main__":
    main()