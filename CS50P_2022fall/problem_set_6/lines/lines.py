import sys

def counter(file):
    try:
        with open(file,'r') as f:
            lines = 0
            for line in f.readlines():
                if line.lstrip().startswith('#') or line.lstrip()=='':
                    continue
                else:
                    lines += 1
        return lines
    except FileNotFoundError:
        sys.exit('File does not exist')

def get_file():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        file_name = sys.argv[1]
        if file_name.split('.')[-1] != 'py':
            sys.exit('Not a python file')
        return file_name

def main():
    file_name = get_file()
    print(counter(file_name))

if __name__=='__main__':
    main()

