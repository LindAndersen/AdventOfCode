def get_inp():    
    with open('input.txt', 'r') as inp:
        inp = [int(x.strip()) for x in inp]
        
    return inp


def find_numbs(inp):
    for i in inp:
        for j in inp:
            for k in inp:
                if j+i+k == 2020:
                    return i*j*k
    
    
    return 'OOpsie'
        
        
def main():
    inp = get_inp()
    rlst = find_numbs(inp)
    

    return rlst

if __name__ == '__main__': print(main())