import sys
from tabulate import tabulate

def get_file():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        file_name = sys.argv[1]
        if file_name.split('.')[-1] != 'csv':
            sys.exit('Not a CSV file')
        else:
            return file_name

def read_file(file):
    try:
        matrix = []
        with open(file,'r') as f:
            for line in f.readlines():
                row = line.strip().split(',')
                matrix.append(row)
        return matrix
    except FileNotFoundError:
        sys.exit('File does not exist')

def main():
    file_name = get_file()
    matrix = read_file(file_name)
    table = matrix[1:]
    headers = matrix[0]
    print(tabulate(table,headers,tablefmt='grid'))

if __name__=='__main__':
    main()



