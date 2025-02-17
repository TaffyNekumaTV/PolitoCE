def main():
    while True:
        try:
            x, y = input('Fraction: ').split('/')
            p = int(x) / int(y) *100
            if p<=1:
                print('E')
            elif p>100:
                continue
            elif p>=99:
                print('F')
            else:
                print(f'{round(p)}%')
            break
        except (ValueError, ZeroDivisionError):
            continue

if __name__=='__main__':
    main()
