import numpy as np

class Solution:
    def __init__(self, filename):
        with open(filename, 'r') as inp:
            outp = []
            for line in inp:
                line = ' '.join(line).split()
                outp.append(line)
        outp = [[int(y) for y in x] for x in outp]
        
        self.arr = np.array(outp)
        self.flashes = 0
        self.lenFlashedNSteps = []
        
        
    def AddOneAround(self, i, j):
        for k in range(-1,2):
            for l in range(-1,2):
                if k != 0 or 0 != l:
                    if i+k == -1 or j+l == -1:
                        continue                        
                    try:
                        self.arr[i+k,j+l] += 1
                    except IndexError:
                        pass
        
    def ChangeFromFlash(self):
        flashedOnce = []
        count = 0
        
        while np.any(self.arr > 9):
            #print(f'Iterations of board:\n{self.arr}')
            try:
                i, j = np.argwhere(self.arr > 9)[count]
            except IndexError:
                print('IndexError')
                break
            if (i,j) in flashedOnce:
                self.arr[i,j] = 0
                count += 1
                continue
            count = 0
            flashedOnce.append((i,j))
            self.arr[i,j] = 0
            self.AddOneAround(i,j)
   
        #print(f'Flashes for this step: {len(flashedOnce)}\n{self.arr}\n')
        self.flashes += len(flashedOnce)
        for (i,j) in flashedOnce:
            self.arr[i,j] = 0
            
        self.lenFlashedNSteps.append(len(flashedOnce))

            
    def nSteps(self, n):
        counter = 0
        while n > counter:
            #print(f'Step no. {counter+1}')
            self.arr += 1
            self.ChangeFromFlash()
            counter += 1
            

def main():
    #s = Solution('example.txt')
    s = Solution('input.txt')
    s.nSteps(500)
    print(s.arr)
    flashes = s.flashes
    
    return flashes, s.lenFlashedNSteps.index(100)+1

if __name__ == '__main__': print(main())