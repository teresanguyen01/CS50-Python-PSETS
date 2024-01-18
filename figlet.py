from pyfiglet import Figlet
import random 
import sys

def main():
    if len(sys.argv) not in [1,3]:
        sys.exit("Invalid usage")
    
    figlet = Figlet()

    if len(sys.argv) == 3: 
        if sys.argv[1] in ["-f", "--font"]:
            font = sys.argv[2]
            if font not in figlet.getFonts():
                sys.exit("Invalid usage")
            figlet.setFont(font=font)
        else:
            sys.exit("Invalid usage")
    elif len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))

    text = input("Input: ")
    print(figlet.renderText(text))

main()








