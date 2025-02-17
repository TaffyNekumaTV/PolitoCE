t = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
while True:
    mark = False
    text = input("Date: ")
    try:
        [x, y, z] = text.split("/")
        m = int(x)
        d = int(y)
        y = int(z)
        if not 1<=m<=12:
            continue
        if not 1<=d<=31:
            continue
        if not 1<=y<=9999:
            continue
        print(f"{y:04}-{m:02}-{d:02}")
        break
    except ValueError:
        mark = True
    try:
        [x, y, z] = text.split()
        m = t[x]
        y = list(y)
        y.pop()
        d = "".join(y)
        d = int(d)
        y = int(z)
        if not 1<=m<=12:
            continue
        if not 1<=d<=31:
            continue
        if not 1<=y<=9999:
            continue
        print(f"{y:04}-{m:02}-{d:02}")
        break
    except KeyError:
        mark = True
    except ValueError:
        mark = True
    if mark:
        continue

