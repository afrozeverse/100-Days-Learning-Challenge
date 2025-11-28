import sys

def average():
    l=[int(x) for x in sys.argv[1::]]
    print(sum(l)/len(l))
average()