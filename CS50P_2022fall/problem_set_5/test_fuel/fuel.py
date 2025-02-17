# def main():
#     while True:
#         try:
#             x, y = input('Fraction: ').split('/')
#             p = int(x) / int(y) *100
#             if p<=1:
#                 print('E')
#             elif p>100:
#                 continue
#             elif p>=99:
#                 print('F')
#             else:
#                 print(f'{round(p)}%')
#             break
#         except (ValueError, ZeroDivisionError):
#             continue

# if __name__=='__main__':
#     main()
def main():
    while True:
        try:
            text = input('Fraction: ')
            p = convert(text)
            print(gauge(p))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    x, y = fraction.split('/')
    if int(y) == 0:
        raise ZeroDivisionError('0')
    if int(x) > int(y):
        raise ValueError()
    p = int(x) / int (y) *100
    return round(p)



def gauge(percentage):
    if percentage <= 1:
        res = 'E'
    elif percentage >=99:
        res = 'F'
    else:
        res = f'{percentage}%'
    return res


if __name__ == "__main__":
    main()
