def get_inp(filename):
    with open(filename, 'r') as inp:
        outp = []
        for line in inp:
            line = ' '.join(line).split()
            outp.append(line)
    outp = [[int(y) for y in x] for x in outp]
    
    return outp

def IncreaseByOne(inp):
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            inp[i][j] += 1
            
    return inp

def FindFirstFlash(inp, flashedList):
    for i, line in enumerate(inp):
        for j, elm in enumerate(line):
            if elm > 9 and (i,j) not in flashedList:
                flashedList.append((i,j))
                return i, j, flashedList
    return -1, -1, flashedList

            
def ChangeFromFlash(inp, i, j):
    inp[i][j] = 0
    
    try:
        inp[i+1][j] += 1
    except:
        pass
    try:
        inp[i+1][j-1] += 1
    except:
        pass    
    try:
        inp[i+1][j+1] += 1
    except:
        pass
    try:
        inp[i][j-1] += 1
    except:
        pass
    try:
        inp[i][j+1] += 1
    except:
        pass
    try:
        inp[i-1][j] += 1
    except:
        pass
    try:
        inp[i-1][j-1] += 1
    except:
        pass
    try:
        inp[i-1][j+1] += 1
    except:
        pass
        
    
    return inp
    
def Step(inp, nSteps):
    flashed = 0
    for _ in range(nSteps):
        print('Step: ' + str(_) + '  Flashed: ' + str(flashed) + '\n\n' + '\n'.join([''.join(list(map(str,x))) for x in inp]) + '\n')
        flashedList = []
        inp = IncreaseByOne(inp)
        i, j, flashedList = FindFirstFlash(inp, flashedList)
        while i != -1 and j != -1:
            inp = ChangeFromFlash(inp, i, j)
            flashed += 1
            i, j, flashedList = FindFirstFlash(inp, flashedList)
            
        
    return flashed
   
    
def main():
    inp = get_inp('input.txt')
    flashed = Step(inp, 10)
    #last answer 3012, too high
    
    return flashed

if __name__ == '__main__': print(main())