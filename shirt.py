import sys
import os 
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3: 
        sys.exit("Too few or too many command-lines")
    elif not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) and not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Not a valid photo file")
    elif not os.path.exists(sys.argv[1]) and not os.path.exists(sys.argv[2]): 
        sys.exit("File not found")
    else: 
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as base_image:
            with Image.open('shirt.png') as shirt_image:
                processed_image = ImageOps.fit(base_image, shirt_image.size)

                processed_image.paste(shirt_image, (0, 0), shirt_image)
            
                processed_image.save(sys.argv[2])

if __name__ == "__main__":
    main()
