import numpy as np
from io import StringIO


def get_inp():
    with open('input.txt','r') as inp:
        output = ''
        for line in inp:
            line = line.replace(' | ',' ')
            output += line
            
    output = np.loadtxt(StringIO(output), dtype='U', delimiter=' ')
    
    
    return output[:,10:]



def find_uniq(arrVals):
    n_uniq = 0
    for output in arrVals:
        for digit in output:
            if len(digit) in [2,4,3,7]:
                n_uniq += 1
                
    return n_uniq
            
            
def main():
    inp = get_inp()
    n = find_uniq(inp)
    
    return n

if __name__ == '__main__': print(main())