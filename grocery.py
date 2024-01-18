def main(): 
    groceries()

def groceries():
    grocery_list = {}

    while True: 
        try:
            items = input().upper()

            if items in grocery_list: 
                grocery_list[items] += 1
            else: 
                grocery_list[items] = 1
    
        except EOFError:
            break
    
    for key in sorted(grocery_list.keys()):
        print(f"{grocery_list[key]} {key}")   

main()
