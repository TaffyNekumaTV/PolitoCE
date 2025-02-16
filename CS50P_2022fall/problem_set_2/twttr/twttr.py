vowels = ['a','i','e','o','u','A','E','I','O','U']

def main():
    text = input('Input: ')
    for c in text:
        if c in vowels:
            continue
        else:
            print(c,end='')

if __name__=='__main__':
    main()
