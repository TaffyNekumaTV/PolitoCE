import sys
from PIL import Image,ImageOps

def get_file():
    if len(sys.argv)>3 :
        sys.exit('Too many arguments')
    elif len(sys.argv) <3:
        sys.exit('Too few arguments')
    else:
        f_in, f_out = sys.argv[1:]
        extension_in = f_in.lower().split('.')[-1]
        extension_out = f_out.lower().split('.')[-1]
        tem = ['jpg', 'png','jpeg']
        if extension_in not in tem:
            sys.exit('Invalid input')
        if extension_out not in tem:
            sys.exit('Invalid output')
        if not extension_in == extension_out:
            sys.exit('Input and output have different extensions')
        return [f_in, f_out]


def main():
    f_in, f_out = get_file()
    print(f_in,f_out)
    try:
        with Image.open(f_in) as im_in, Image.open('shirt.png') as shirt:
            shirt_size = shirt.size
            new_in = ImageOps.fit(im_in,shirt_size)
            new_in.paste(shirt,(0,0),shirt)
            new_in.save(f_out)

    except FileNotFoundError:
        sys.exit('File does not exist')


if __name__=='__main__':
    main()

