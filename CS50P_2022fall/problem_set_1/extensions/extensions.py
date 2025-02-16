name = {'gif':'image/gif',
        'jpg':'image/jpeg',
        'jpeg':'image/jpeg',
        'png':'image/png',
        'pdf':'application/pdf',
        'txt':'text/plain',
        'zip':'application/zip'
        }

def get_suffix(file_name):
    return file_name.strip().lower().split('.')[-1]

def main():
    file = input('File name: ')
    file_name = get_suffix(file)
    if file_name in name.keys():
        print(name[file_name])
    else:
        print('application/octet-stream')

if __name__=='__main__':
    main()
