def main():
    print("Amount Due: 50")
    coins = int(input("Insert Coin: "))
    cokeMachine(coins)


def cokeMachine(coins):
    amountDue = 50
    change = 0
    while (amountDue != 0):
        if (coins == 25 or coins == 10 or coins == 5):
            amountDue -= coins
        
        if amountDue <= 0:
            while amountDue < 0: 
                change += 1
                amountDue += 1
            print("Change Owed:", change)

        if amountDue == 0: 
            break 
        else: 
            print("Amount Due:", amountDue)
        coins = (int(input("Insert Coin: ")))
    
main()
