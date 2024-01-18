import random

def main():
    level = get_level()
    score = 0 
    
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        correct_answer = x + y

        for attempt in range(3):
            try: 
                user_answer = int(input(f"{x} + {y} = "))

                if user_answer == correct_answer: 
                    score += 1
                    break
                else: 
                    print("EEE")
            except ValueError:
                print("EEE")
        if user_answer != correct_answer:
            print(f"{x} + {y} = {correct_answer}")
        
    print(f"Score: {score}")

def get_level():
    while True: 
        try: 
            levels = int(input("Level: "))
            if levels in [1, 2, 3]:
                return levels
            else: 
                levels = input("Level: ")
        except ValueError:
            continue

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError()
    if level == 1: 
        return random.randint(0,9)
    if level == 2: 
        return random.randint(10,99)
    if level == 3: 
        return random.randint(100,999)


if __name__ == "__main__":
    main()