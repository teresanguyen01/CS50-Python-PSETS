import csv
import sys
import os

def main(): 
    if len(sys.argv) != 3:
        sys.exit("exit")
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv"):
        sys.exit("exit")
    if not os.path.exists(input_file): 
        sys.exit(f"Could not read {input_file}")

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile: 
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        writer.writerow(['first', 'last', 'house'])

        for row in reader:
            if len(row) != 2:
                continue
            name, house = row
            try:
                last, first = name.split(", ")
                writer.writerow([first, last, house])
            except ValueError:
                continue 

if __name__ == "__main__":
    main()

