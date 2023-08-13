class Solution:
    def __init__(self,filename):
        self.data = self.ReadData(filename)
        self.numberOfContainedRanges = self.FindNumberOfContainedRanges()
        self.numberOfOverlappingRanges = self.FindNumberOfOverlappingRanges()
        
        
    def ReadData(self, filename):
        data = []
        with open(filename, 'r') as f:
            for line in f:
                newLine = list(map(int,line.replace('-',' ').replace(',',' ').split()))
                data.append(newLine)
                
        return data
                
                
    def FindNumberOfContainedRanges(self):
        n = 0
        for [r1start,r1end,r2start,r2end] in self.data:
            if r1start >= r2start and r1end <= r2end:
                n += 1
            elif r1start <= r2start and r1end >= r2end:
                n += 1
                
                
        return n
                
    def FindNumberOfOverlappingRanges(self):
        n = 0
        
        for [r1start,r1end,r2start,r2end] in self.data:
            r1 = range(r1start,r1end+1)
            r2 = range(r2start,r2end+1)
            if set(r1).intersection(r2) != set():
                n += 1
            
        return n
        
        
        
def main():
    s = Solution('input.txt')
    print(s.data)
    
    
    return s.numberOfOverlappingRanges


if __name__ == '__main__':print(main())