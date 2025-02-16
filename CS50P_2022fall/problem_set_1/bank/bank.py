def main():
    d = 100
    text = input('Greeting: ').lstrip().lower()
    if text[0] == 'h':
        d = 20
        if text[0:5] == 'hello':
            d = 0
    print(f'${d}')

if __name__=='__main__':
    main()
