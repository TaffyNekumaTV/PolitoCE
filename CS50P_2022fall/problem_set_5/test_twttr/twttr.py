vowels = ['a','i','e','o','u','A','E','I','O','U']

# def main():
#     text = input('Input: ')
#     for c in text:
#         if c in vowels:
#             continue
#         else:
#             print(c,end='')

# if __name__=='__main__':
#     main()

def main():
    text = input('Input: ')
    print(shorten(text))


def shorten(word):
    new_word = []
    for c in word:
        if c in vowels:
            continue
        else:
            new_word.append(c)
    return ''.join(new_word)


if __name__ == "__main__":
    main()
