import inflect
p = inflect.engine()

def main():
    adieu_function()

def adieu_function():
    list_of_names = []
    while True: 
        try: 
            name = input("")
            if name: 
                list_of_names.append(name)
        except EOFError:
            break
    print("Adieu, adieu, to", p.join(list_of_names))
    
main()