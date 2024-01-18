    # Roman Numeral / Number Converter
    #### Video Demo:  <https://youtu.be/Pq15V9GtrWc>
    #### Description:
    This is a program that allows users to convert numbers to Roman numerals, Roman numerals to numbers, and also to generate a random Roman numeral within a specific range (1-1000). This script is particularly useful for educational purposes, historical research, or simply as a fun tool to explore the ancient numeral system.

The script starts by defining a dictionary, roman_numerials, which maps integers (from 1 to 1000) to their corresponding Roman numeral representations. This dictionary serves as the core data structure for the program, enabling quick conversions between numbers and Roman numerals.

The main() function is the entry point of the script. It presents users with three choices:

1 Convert a number (between 1 and 1000) to its Roman numeral equivalent.
2 Convert a Roman numeral (representing numbers 1-1000) back to its number equivalent.
3 Generate a random Roman numeral within the range of 1 to 1000.
For the first option, the user is prompted to enter a number. The script ensures that the input is a valid integer within the specified range. If the input meets these criteria, the script calls the convert_to_numerals function, which retrieves the corresponding Roman numeral from the roman_numerials dictionary.

The second option caters to converting a Roman numeral input back to a number. The user inputs a Roman numeral, and the convert_to_number function iterates through the dictionary to find the matching number. This function demonstrates the versatility of the script in handling the reverse process of the numeral system.

The third option is a unique feature that generates a random Roman numeral. If the user chooses this option, the random_roman function is invoked. This function uses Python's random library to select a random integer between 1 and 1000 and then fetches the corresponding Roman numeral from the dictionary.

The script employs robust error handling to manage invalid inputs and ensures that the user inputs are in the expected format. This includes handling non-integer inputs for number conversion and ensuring that the Roman numeral input consists only of alphabetical characters. The script loops until a valid input is received, enhancing user experience by avoiding abrupt terminations due to incorrect inputs.

Furthermore, the script is a practical application of Python's fundamental concepts like dictionaries, functions, loops, conditional statements, and exception handling. It showcases the effective use of a dictionary to map relationships between different data types – in this case, integers and strings (Roman numerals).





