from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv)==1:
        text = input('Input: ')
        f = random.choice(fonts)
        figlet.setFont(font=f)
        print(figlet.renderText(text))
    elif len(sys.argv)==3:
        if sys.argv[1] not in ['-f','--font'] or sys.argv[2] not in fonts:
            sys.exit('Invalid usage')
        else:
            text = input('Input: ')
            f = sys.argv[2]
            figlet.setFont(font=f)
            print(figlet.renderText(text))
    else:
        sys.exit('Invalid usage')

if __name__=='__main__':
    main()

