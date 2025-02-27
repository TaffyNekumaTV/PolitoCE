def main():
    grocery_list = {}
    while True:
        try:
            item = input().strip().upper()
            if item not in grocery_list:
                grocery_list[item]=0
            grocery_list[item] += 1
        except EOFError:
            break
    for item in sorted(grocery_list):
        print(f'{grocery_list[item]} {item}')

if __name__=='__main__':
    main()


