import numpy as np
from io import StringIO

def get_inp():
    with open('input.txt','r') as inp:
       outp = inp.read().replace('-', ' ').replace(':', '')
       
    inp = np.loadtxt(StringIO(outp), dtype='U', delimiter=' ')
    
    return inp


def is_valid_pass(pos1, pos2, letter, passw):
    pos1 = int(pos1)-1
    pos2 = int(pos2)-1
    
    if (passw[pos1] == letter and not passw[pos2] == letter) or (passw[pos2] == letter and not passw[pos1] == letter):
        return True
    return False


def find_valid_pass(inp):
    count = 0
    for i in inp:
        if is_valid_pass(i[0], i[1], i[2], i[3]):
            count += 1
            
    return count


def main():
    inp = get_inp()
    n = find_valid_pass(inp)
    
    

    return n


if __name__ == '__main__': print(main())