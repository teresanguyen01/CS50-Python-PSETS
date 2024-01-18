
def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date_input = input("Enter a date (e.g., 9/8/1636 or September 8, 1636): ")
        try:
            if '/' in date_input:
                month, day, year = map(int, date_input.split('/'))
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            elif ',' in date_input:
                parts = date_input.replace(',', '').split()
                if len(parts) == 3 and parts[0] in months and parts[1].isdigit() and parts[2].isdigit():
                    month = months.index(parts[0]) + 1
                    day = int(parts[1])
                    year = int(parts[2])
                    if 1 <= day <= 31:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
            else:
                continue
        except ValueError:
            continue
        
main()


