import numpy as np
from io import StringIO

def get_inp():
    with open('input.txt','r') as inp:
       outp = inp.read().replace('-', ' ').replace(':', '')
       
    inp = np.loadtxt(StringIO(outp), dtype='U', delimiter=' ')
    
    return inp


def is_valid_pass(min_o, max_o, letter, passw):
    count = 0
    for char in passw:
        if char == letter:
            count += 1
    if int(min_o) <= count <= int(max_o):
        return True
    return False


def find_valid_pass(inp):
    count = 0
    for i in inp:
        print(i)
        if is_valid_pass(i[0], i[1], i[2], i[3]):
            count += 1
            
    return count


def main():
    inp = get_inp()
    n = find_valid_pass(inp)
    
    

    return n


if __name__ == '__main__': print(main())