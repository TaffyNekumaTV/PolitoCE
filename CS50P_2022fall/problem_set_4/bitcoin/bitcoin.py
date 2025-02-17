import requests
import sys

def main():
    try:
        n = float(sys.argv[1])
        r = requests.get('https://api.coincap.io/v2/assets/bitcoin')
        amount = float(r.json()['data']['priceUsd']) *n
        print(f"${amount:,.4f}")

    except ValueError:
        sys.exit('Command-line argument is not a number')

if __name__=='__main__':
    main()
