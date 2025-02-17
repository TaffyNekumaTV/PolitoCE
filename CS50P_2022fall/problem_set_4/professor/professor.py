import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level),generate_integer(level)
        res = x + y
        chance = 3
        while chance > 0:
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer != res:
                    chance -= 1
                    print('EEE')
                    continue
                else:
                    score += 1
                    break
            except ValueError:
                chance -=1
                print('EEE')
                continue
        if chance == 0:
            print(f'{x} + {y} = {res}')
    print(f'Score: {score}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1,2,3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    return random.randrange(0 if level==1 else 10**(level-1), 10**level)



if __name__ == "__main__":
    main()
