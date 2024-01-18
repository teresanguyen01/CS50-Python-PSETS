def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    wo_dollar = d.replace("$", "")
    return(float(wo_dollar))

def percent_to_float(p):
    wo_percent = p.replace("%", "")
    return(float(wo_percent) / 100)

main()