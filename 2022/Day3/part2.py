import string
import math

class Solution:
    def __init__(self,filename):
        self.data = self.ReadData(filename)
        self.commonParts = []
        self.score = 0
        
        
    def ReadData(self,filename):
        data = []
        inter = []
        
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                inter.append(line)
                if len(inter) == 3:
                    data.append(inter)
                    inter = []
                
        return data
    
    def FindCommonParts(self):
        
        for [elf1,elf2,elf3] in self.data:
            for part in elf1:
                if part in elf2 and part in elf3:
                    self.commonParts.append(part)
                    break
                    
        
        
    def FindCommonPartsScore(self):
        scoreDict = {}
        
        for i in range(1,27):
            scoreDict[list(string.ascii_lowercase)[i-1]] = i
        for i in range(27,53):
            scoreDict[list(string.ascii_uppercase)[i-27]] = i
        
        for part in self.commonParts:
            self.score += scoreDict[part]
    
    
    
def main():
    s = Solution('input.txt')
    s.FindCommonParts()
    s.FindCommonPartsScore()
    print(s.score)
    
    
    
    return f'{s.data[0:2]}\n\n{s.commonParts[0:2]}'


if __name__ == '__main__': print(main())