import sys
import os

def main():
    print(length_reader())

def length_reader():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 3: 
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    else: 
        filename = sys.argv[1] 
        if not os.path.exists(filename):
            sys.exit("Error: File does not exist")
        else:
            count = 0
            with open(filename, 'r') as file:
                for line in file:
                    stripped_line = line.strip()
                    if stripped_line and not stripped_line.startswith('#'):
                        count+=1 
    return count

if __name__ == "__main__":
    main()