"""x = int(input("What is x? "))
y = int(input("What is y? "))

# boolean expression
 if x < y:
    print("x is less than y")
elif x > y: 
    print("x is greater than y")
else: 
    print("x is equal to y")


if x != y: 
    print("x is not equal to y")
else:
    print("x is equal to y")"""

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("is even")
    else:
        print("odd")
def is_even(n):
    if n % 2 == 0: 
        return True
    else: 
        return False
    
main()