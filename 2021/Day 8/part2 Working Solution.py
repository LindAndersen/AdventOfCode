import numpy as np
from io import StringIO
       

def get_inp():
    with open('input.txt','r') as inp:
        output = ''
        for line in inp:
            line = line.replace(' | ',' ')
            # Alphabetic sort so the output digits can be read easily once digits are determined
            output += ' '.join([''.join(sorted(elm)) for elm in line.split()]) + '\n'
            
    output = np.loadtxt(StringIO(output), dtype='U', delimiter=' ')
    
    return output[:,:10], output[:,10:]

def sub_string(a, b): #if b contains a return True else False
    for i in a:
        if i in b:
            continue
        else:
            return False
    return True

def find_numbers(line):
    config = {}
    fives = []
    sixes = []
    
    for digit in line:
        if len(digit) == 2:
            config[digit] = 1
        elif len(digit) == 3:
            config[digit] = 7
        elif len(digit) == 4:
            config[digit] = 4
        elif len(digit) == 7:
            config[digit] = 8
        elif len(digit) == 5:
            fives.append(digit)
        elif len(digit) == 6:
            sixes.append(digit)
    
    inv_config = {k: v for v, k in config.items()}
    
    for i in sixes:
        if sub_string(inv_config[4], i):
            config[i] = 9
        elif sub_string(inv_config[7], i):
            config[i] = 0
        else:
            config[i] = 6
            
    inv_config = {k: v for v, k in config.items()}
    
    for i in fives:
        if sub_string(inv_config[1], i):
            config[i] = 3
        elif sub_string(i, inv_config[9]):
            config[i] = 5
        else:
            config[i] = 2
        
                
    return config

def get_out_number(config, outp):
    n = ''
    for digit in outp:
        n += str(config[digit])

    return int(n)

            
def main():
    n = 0
    inp, outp = get_inp()
    
    for index, line in enumerate(inp):
        config = find_numbers(line)
        n += get_out_number(config, outp[index])
    
    return n

if __name__ == '__main__': print(main())