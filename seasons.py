import re
from datetime import date, datetime
import sys
import inflect
p = inflect.engine()

def main(): 
    date_input = input("Input: ")
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    if not date_pattern.match(date_input):
        sys.exit("Invalid date format. Exiting program.")
    else: 
        print(seasons_function(date_input))

def seasons_function(date_input):
    year, month, day = date_input.split("-")
    difference_in_dates = date.today() - date(int(year), int(month), int(day))
    number_of_days, extra1, extra2 = str(difference_in_dates).split(" ")
    number_of_minutes = int(number_of_days) * 24 * 60
    return((p.number_to_words(number_of_minutes).capitalize().replace(" and ", " ")) + " minutes")

if __name__ == "__main__":
    main()
        
