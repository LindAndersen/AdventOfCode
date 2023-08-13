import numpy as np
from io import StringIO
       

def get_inp():
    with open('input.txt','r') as inp:
        output = ''
        for line in inp:
            line = line.split()
            output += ','.join(line[0]) + '\n'

        output = np.loadtxt(StringIO(output), dtype='i', delimiter=',')
        
    return output

def get_inp_fromstring(string):
    string = ' '.join(string)
    inp = np.fromstring(string, dtype=int, sep=' ').reshape(-1,10)
    
    return inp

def add_nines(inp):
    new = np.zeros((len(inp)+2, len(inp[0,:])+2), dtype=int)
    new[0,:] = 9
    new[len(new)-1,:] = 9
    new[:,0] = 9
    new[:,len(new[0,:])-1] = 9
    
    
    for i, line in enumerate(inp):
        new[i+1,1:len(line)+1] = line
    
    return new, inp


def is_low_point(elm, i, j, arr):
    if arr[i+1,j] <= elm or arr[i, j-1] <= elm or arr[i-1, j] <= elm or arr[i, j+1] <= elm:
        return False
    
    
    return True


def find_low_points(new, inp):
    low_points = []
    for i, line in enumerate(inp):
        for j, elm in enumerate(line):
            if is_low_point(elm, i+1, j+1, new):
                low_points.append((i,j))
    return low_points

class Node:
    visitedNodes = []
    new = ''
    
    def __init__(self, coord):
        self.coord = coord
        i, j = coord
        self.up = i+1,j
        self.down = i-1,j
        self.left = i,j-1
        self.right = i, j+1

def FindChildren(node):
    if Node.new[node.up] != 9 and node.up not in Node.visitedNodes:
        Node.visitedNodes.append(node.up)
        FindChildren(Node(node.up))
    
    if Node.new[node.down] != 9 and node.down not in Node.visitedNodes:
        Node.visitedNodes.append(node.down)
        FindChildren(Node(node.down))
        
    if Node.new[node.left] != 9 and node.left not in Node.visitedNodes:
        Node.visitedNodes.append(node.left)
        FindChildren(Node(node.left))
        
    if Node.new[node.right] != 9 and node.right not in Node.visitedNodes:
        Node.visitedNodes.append(node.right)
        FindChildren(Node(node.right))
        
        
def FindBasins(lowPoints, new):
    Node.new = new
    basinsLength = []
    for i, j in lowPoints:
        coord = i+1, j+1
        Node.visitedNodes = []
        a = Node(coord)
        Node.visitedNodes.append(a.coord)
        FindChildren(a)
        print([Node.new[i,j] for i,j in Node.visitedNodes])
        print(Node.visitedNodes)
        basinsLength.append(len(Node.visitedNodes))
        
        
    return basinsLength

def FindBiggest(basinsLength):
    big = basinsLength[:3]
    for elm in basinsLength[3:]:
        if elm > min(big):
            big[big.index(min(big))] = elm
    return big


def main():
    #inp = '2199943210\n3987894921\n9856789892\n8767896789\n9899965678'
    #inp = get_inp_fromstring(inp)
    inp = get_inp()
    new, inp = add_nines(inp)
    low_points = find_low_points(new, inp)
    print('Low points: ' + str(low_points) + '\n')
    basinsLength = FindBasins(low_points, new)
    top3 = FindBiggest(basinsLength)
    print('\nBasins lengths: ' + str(basinsLength))
    print('\nTop 3: ' + str(top3))
    rlst = np.prod(top3)
    
    return rlst




if __name__ == '__main__': print(main())