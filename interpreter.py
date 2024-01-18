expression = input("Expression: ").strip()
x, y, z = expression.split(" ")

if y == "/":
    print(round(float(int(x) / int(z)), 1))
elif y == "+":
    print(round(float(int(x) + int(z)), 1))
elif y == "-":
    print(round(float(int(x) - int(z)), 1))
elif y == "*":
    print(round(float(int(x) * int(z)), 1))
