import random

def main():
    while True:
        try:
            level = int(input('Level: '))
            if level>0:
                break
        except ValueError:
            continue
    goal = random.randrange(1,(level+1))
    while True:
        try:
            guess = int(input('Guess: '))
            if guess <= 0:
                continue
            if guess > goal:
                print('Too large!')
                continue
            elif guess < goal:
                print('Too small!')
            else:
                print('Just right!')
                break
        except ValueError:
            continue

if __name__=='__main__':
    main()
