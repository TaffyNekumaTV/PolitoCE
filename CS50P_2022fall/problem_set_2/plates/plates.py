def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    res = True
    if len(s) > 6 or len(s) < 2:
        res = False
    if not s[0:2].isalpha():
        res = False
    if len(s) > 2:
        for c in s:
            if c.isalpha():
                continue
            if c.isnumeric():
                if int(c)==0:
                    res = False
                break
    if len(s) > 2:
        for i in range(2,len(s)):
            if s[i].isnumeric():
                if not s[i:].isnumeric():
                    res = False
    return res



main()
