class Solution:
    def __init__(self,filename):
        self.data = self.ReadData(filename)
        
    def ReadData(self, filename):
        data = []
        with open(filename, 'r') as f:
            for line in f:
                data.append((line[0],line[2]))
        
        return data
        
    def CalcScore(self):
        score = 0
        
        p1Trans = {'A':'X','B':'Y','C':'Z'}
        evalWin = {'X':'Z','Y':'X','Z':'Y'}
        evalPoint = {'X':1,'Y':2,'Z':3}
        for (p1,p2) in self.data:
            p1 = p1Trans[p1]
            #losing condition
            if evalWin[p1] == p2:
                score += evalPoint[p2]
            #draw condition
            elif p1 == p2:
                score += 3 + evalPoint[p2]
            #winning condition
            else:
                score += 6 + evalPoint[p2]
                
                
        return score
        
    
    def CalcScore2(self):
        score = 0
        
        evalMove = {'A':'C','B':'A','C':'B'}
        evalMove1 = {}
        for k,v in evalMove.items():
            evalMove1[v] = k
        evalPoint = {'A':1,'B':2,'C':3}
        for (p1,p2) in self.data:
            #losing condition
            if p2 == 'X':
                score += evalPoint[evalMove[p1]]
            #draw condition
            elif p2 == 'Y':
                score += 3 + evalPoint[p1]
            #winning condition
            else:
                score += 6 + evalPoint[evalMove1[p1]]
                
                
        return score
    
    
def main():
    s = Solution('input.txt')
    scorepart1 = s.CalcScore()
    scorepart2 = s.CalcScore2()
    
    return scorepart2

if __name__ == '__main__': print(main())