import requests
import sys

while True: 
    try: 
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
            break
        elif len(sys.argv) == 2 and sys.argv[1].isalpha():
            sys.exit("Command-line argument is not a number")
            break
        else:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            response.raise_for_status()
            data = response.json()
            price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
            cost_of_bitcoin = float(sys.argv[1]) * price_per_bitcoin

            print(f"${cost_of_bitcoin:,.4f}")
            break
    except requests.RequestException:
        break