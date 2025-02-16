d = {
    "apple":130,
    "banana":110,
    "grapefruit":60,
    "honeydewmelon":50,
    "lemon":15,
    "nectarine":60,
    "Pineapple":50,
    "strawberrie":50,
    "tangerine":50,
    "peach":60,
    "avocado":50,
    "cantaloupe":50,
    "grapes":90,
    "kiwifruit":90,
    "lime":20,
    "orange":80,
    "pear":100,
    "plums":70,
    "sweet cherries":100,
    "watermelon":80
}
def main():
    k = input("Item: ").lower()
    if k in d:
        print(f"Calories: {d[k]}")

if __name__=='__main__':
    main()
