import csv,sys

def get_file():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    else:
        files = sys.argv[1:]
        for file in files:
            if file.split('.')[-1] != 'csv':
                sys.exit('Not a CSV file')
        return files

def main():
    try:
        f_in, f_out = get_file()
        print(f_out)
        with open(f_in, 'r') as f1,open(f_out,'w') as f2:
            reader = csv.DictReader(f1)
            writer = csv.DictWriter(f2,fieldnames=['first','last','house'])
            writer.writeheader()
            for row in reader:
                name = row['name']
                house = row['house']
                last, first = name.split(', ')
                writer.writerow({'first':first, 'last':last,'house':house})

    except FileNotFoundError:
        sys.exit(f'Could not read {f_in}')

if __name__=='__main__':
    main()

