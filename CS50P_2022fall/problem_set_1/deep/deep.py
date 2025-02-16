forty_two = ['forty-two','forty two','42']

def main():
    text =input('What is the Answer to the Great Question of Life, the Universe and Everything?').strip().lower()
    if text in forty_two:
        print('Yes')
    else:
        print('No')

if __name__=='__main__':
    main()
