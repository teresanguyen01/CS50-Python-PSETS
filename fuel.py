"""def main():
    fuel_tank()

def fuel_tank():
    while True:
        try: 
            fraction_ = input("Fraction: ")
            x, y = fraction_.split("/")

            if (int(x) > int(y) or int(y) == 0):
                raise ValueError

            fuel_percentage = round(int(x) / int(y) * 100)

            if fuel_percentage <= 1: 
                print("E")
                break
            elif fuel_percentage >= 99: 
                print("F")
                break
            else: 
                print(f"{fuel_percentage}%")
                break

        except (ValueError, ZeroDivisionError):
            continue

main()"""

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            fraction_ = convert(fraction)
            print(gauge(fraction_))
            break  
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = fraction.split("/")
    if int(x) > int(y): 
        raise ValueError
    if int(y) == 0: 
        raise ZeroDivisionError
    return round(int(x) / int(y) * 100, 2)

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else: 
        return(f"{percentage}%")


if __name__ == "__main__":
    main()
            
        