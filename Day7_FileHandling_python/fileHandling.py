def write_to_file(filename, data):
    f= open(filename,'w')
    f.write(data)
    f.close()

def append_to_file(filename, data):
    f= open(filename,'a')
    data='\n'+data
    f.write(data)
    f.close()

def read_from_file(filename):
    try:
        f= open(filename,'r')
        data=f.read()
        print(data)
    except FileNotFoundError:
        print("Fle not found!")
    f.close()


def main():
    data=input("Enter the data:")
    write_to_file('file.txt',data)

if __name__ == "__main__":
    main()