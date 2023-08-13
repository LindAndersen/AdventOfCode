import string

class Solution:
    def __init__(self,filename):
        self.data = self.ReadData(filename)
        
        
    def ReadData(self,filename):
        data = []
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                splitIndex = int(len(line)/2)
                c1 = line[0:splitIndex]
                c2 = line[splitIndex:]
                data.append((c1,c2))
                
        return data
    
    def FindCommonParts(self):
        commonParts = []
        for (c1,c2) in self.data:
            for part in c1:
                if part in c2:
                    commonParts.append(part)
                    break
                    
        return commonParts
                    
        
        
    def FindCommonPartsScore(self, commonParts):
        score = 0
        scoreDict = {}
        
        for i in range(1,27):
            scoreDict[list(string.ascii_lowercase)[i-1]] = i
        for i in range(27,53):
            scoreDict[list(string.ascii_uppercase)[i-27]] = i
        print(scoreDict)
        
        for part in commonParts:
            score += scoreDict[part]
        
        return score
    
    
    
def main():
    s = Solution('input.txt')
    parts = s.FindCommonParts()
    score = s.FindCommonPartsScore(parts)
    
    
    
    return score


if __name__ == '__main__': print(main())