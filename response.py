import validators 

def main(): 
    print(response(input("What is your email? ")))
          
def response(s): 
    if validators.email(s):
        return("Valid")
    else: 
        return("Invalid")

if __name__ == "__main__":
    main()