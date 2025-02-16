def main():
    text = input('camelCase: ')
    for c in text:
        if c.islower():
            print(c, end='')
        else:
            print(f'_{c.lower()}',end='')


if __name__=='__main__':
     main()
