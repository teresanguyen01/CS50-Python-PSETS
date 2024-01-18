import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if " to " not in s: 
        raise ValueError("Unable to parse")

    begin_time, end_time = s.split(" to ")

    def process_time(time_str):
        match = re.match(r"^(\d+)(?::(\d{2}))? (AM|PM)", time_str)
        if not match:
            raise ValueError("Invalid time format")

        hour, minute, period = match.groups()
        hour = int(hour)
        minute = int(minute) if minute else 0

        if period == "PM" and hour != 12:
            hour += 12
        elif period == "AM" and hour == 12:
            hour = 0

        return "{:02d}:{:02d}".format(hour, minute)

    formatted_begin_time = process_time(begin_time)
    formatted_end_time = process_time(end_time)
 
    return f"{formatted_begin_time} to {formatted_end_time}"

if __name__ == "__main__":
    main()
