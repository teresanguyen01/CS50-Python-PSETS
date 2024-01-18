#from tabulate import tabulate
import sys
import os
import csv
import tabulate

def main():
    print(table_open())

def table_open():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    elif not os.path.exists(sys.argv[1]):
        sys.exit("File does not exist")
    else: 
        filename = sys.argv[1]
        with open(filename, 'r') as file: 
            readers = csv.reader(file)
            rows = list(readers)
            return(tabulate.tabulate(rows, headers="firstrow", tablefmt="grid"))
        
if __name__ == "__main__":
    main()
            

