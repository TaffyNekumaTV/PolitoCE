menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def main():
    total = 0
    while True:
        try:
            item = input('Item: ').lower()
            price = menu[item]
            total += price
            print(f'Total: ${total:.2f}')
        except KeyError:
            continue
        except EOFError:
            break

if __name__=='__main__':
    main()

