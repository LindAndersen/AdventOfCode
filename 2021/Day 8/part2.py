import numpy as np
from io import StringIO

def get_inp_out():
    with open('input.txt','r') as inp:
        output = ''
        for line in inp:
            line = line.replace(' | ',' ')
            output += line
            
    output = np.loadtxt(StringIO(output), dtype='U', delimiter=' ')
    
    
    return output[:,:10], output[:,10:]

def update_logic(new, *args):
    print('this is args: {}\n'.format(args))
    char_list = [x for x in new]
    update_list = []
    for i in range(len(args)):
        update = ''
        if args[i] == '':
            update_list.append(new)
            continue
        for char in args[i]:
            print(char)
            if char in char_list:
                update += char
        update_list.append(update)
    
    return update_list


def find_config(segment, output):
    config = np.empty(7, dtype='U')
    for elm in segment:
        print(elm, len(elm))
        if len(elm) == 2:
            #1
            update_list = update_logic(elm, config[2], config[5])
            config[2] = update_list[0]
            config[5] = update_list[1]
                
        elif len(elm) == 3:
            #7
            update_list = update_logic(elm, config[0], config[2], config[5])
            config[0] = update_list[0]
            config[2] = update_list[1]
            config[5] = update_list[2]
        elif len(elm) == 4:
            #4
            update_list = update_logic(elm, config[1], config[2], config[3], config[5])
            config[1] = update_list[0]
            config[2] = update_list[1]
            config[3] = update_list[2]
            config[5] = update_list[3]
        elif len(elm) == 5:
            #2,3,5
            pass
        elif len(elm) == 6:
            #6,9,0
            pass
        elif len(elm) == 7:
            #8
            update_list = update_logic(elm, config[0], config[1], config[2], config[3], config[4], config[5], config[6])
            for i in range(7):
                config[i] = update_list[i]
                
        #print(config)
    
    return config
                

         
def main():
    inp, out = get_inp_out()
    
    for i in range(1):
    #for i in range(len(inp)):
        config = find_config(inp[i],out[i])
    
    
    
    
    return config

if __name__ == '__main__': main()



























