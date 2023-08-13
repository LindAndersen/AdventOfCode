import numpy as np

def get_input():
    with open('input.txt','r') as inp:
        coords = ''
        for index, line in enumerate(inp):
            line = line.replace(' -> ', ',')
            coords += line.replace('\n', ',')
        
    coords = np.fromstring(coords, dtype=int, sep=',').reshape(500,4)
    
    return coords

def insert_line(dia, lock, c1, c2, ID, *args):
    if ID == 'h':
        for index, el in enumerate(dia[lock][c1:c2+1]):
            if el != 0:
                dia[lock][index+c1] += 1
            else:
                dia[lock][index+c1] = 1
    elif ID == 'v':
        for index, el in enumerate(dia[c1:c2+1]):
            if el[lock] != 0:
                dia[index+c1][lock] += 1
            else:
                dia[index+c1][lock] = 1
    elif ID == 'd':
        x1, y1, x2, y2 = lock, c1, c2, args[0]
        diffx, diffy = x2-x1, y2-y1
        #print(x1, x2, y1, y2)
        #print(diffx, diffy)
        for i in range(abs(diffx)+1):
            if diffx > 0 and diffy > 0:
                y,x = y1+i,x1+i
            elif diffx > 0 and diffy < 0:
                y, x = y1-i,x1+i
            elif diffx < 0 and diffy > 0:
                y, x = y1+i,x1-i
            elif diffx < 0 and diffy < 0:
                y, x = y1-i,x1-i
            else:
                print('somethings off')
            
            if dia[y,x] != 0:
                dia[y,x] += 1
            else:
                dia[y,x] = 1
        #print('({},{}) -> ({},{})'.format(x1, x2, y1, y2))
        
    
    return dia

def make_diagram(coords):
    dia = np.zeros(shape=(1000,1000))
    
    for x1, y1, x2, y2 in coords:
        if x1 == x2:
            if y1 > y2: 
                y1, y2 = y2, y1
            dia = insert_line(dia, x1, y1, y2, 'v')
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            dia = insert_line(dia, y1, x1, x2, 'h')
        else:
            dia = insert_line(dia, x1, y1, x2, 'd', y2)
            
    return dia
        
def count(dia):
    return (dia >= 2).sum()
    
def main():
    coords = get_input()
    dia = make_diagram(coords)
    result = count(dia)
    
    return result


if __name__ == '__main__': print(main())