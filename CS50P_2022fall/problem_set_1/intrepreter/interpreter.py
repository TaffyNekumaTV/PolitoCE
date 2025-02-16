def main():
    text = input('Exprissions: ')
    x, y, z = text.split(' ')
    x, z =float(x), float(z)
    match y :
        case '+':
            res = x + z
        case '-':
            res = x - z
        case '*':
            res = x * z
        case '/':
            res = x / z
    print(f'{res:.1f}')

if __name__=='__main__':
    main()
