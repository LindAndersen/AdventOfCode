import numpy as np
from io import StringIO

def get_inp_out():
    with open('input.txt','r') as inp:
        output = ''
        for line in inp:
            line = line.replace(' | ',' ')
            output += line
            
    inp = np.loadtxt(StringIO(output), dtype='U', delimiter=' ')
    
    
    return inp


def step_is_possible(old, new):
    return 0

def update_config(config, seg, new):
    return 0

def make_path(line):
    path = {}
    for i in range(len(line)):
        if len(line[i]) in [2,3,4,7]:
            path[i] = (0,-1,-1)
        else:
            path[i] = (0,0,0)
    
    return path

def go_back(path):
    for i in path.__reversed__():
        if 0 in path[i]:
            n = path[i].index(0)
            break
    
    return n, i
    

def find_config(line):
    config = np.empty(7, dtype='U')
    path = make_path(line)
    
    n, i = go_back(path)
    
    print(n, i)
    
    print(path)
    
    return config

def calc_output(config, output):
    n = 0
    return n


def main():
    inp = get_inp_out()
    
    for line in inp:
        find_config(line)
        break
    
    
    
    return inp

if __name__ == '__main__': main()