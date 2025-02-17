# def main():
#     d = 100
#     text = input('Greeting: ').lstrip().lower()
#     if text[0] == 'h':
#         d = 20
#         if text[0:5] == 'hello':
#             d = 0
#     print(f'${d}')

# if __name__=='__main__':
#     main()

def main():
    text = input('Greeting: ').lstrip()
    print(f'${value(text)}')


def value(greeting):
    d = 100
    if greeting[0].lower() == 'h':
        d =20
        if greeting[0:5].lower() == 'hello':
            d = 0
    return d



if __name__ == "__main__":
    main()
