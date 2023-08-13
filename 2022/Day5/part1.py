class Solution:
    def __init__(self,filename):
        self.config, self.moves = self.ReadData(filename)
        self.topOfStacks = self.FindTopOfStacks()
        
        
    def ReadData(self,filename):
        config = {}
        moves = []
        with open(filename,'r') as f:
            for line in f:
                if line == '\n':
                    break
                
                line = line.replace('[','').replace(']','')
                for elm in line:
                    pass
            config = {1:['R','G','J','B','T','V','Z'],2:['J','R','V','L'],3:['S','Q','F'],4:['Z','H','N','L','F','V','Q','G'],5:['R','Q','T','J','C','S','M','W'],6:['S','W','T','C','H','F'],7:['D','Z','C','V','F','N','J'],8:['L','G','Z','D','W','R','F','Q'],9:['J','B','W','V','P']}
            #config = {1:['Z','N'],2:['M','C','D'],3:['P']}
            
            
            inter = []
            for line in f:
                line = line.split()
                inter.append(int(line[1]))
                inter.append(int(line[3]))
                inter.append(int(line[5]))
                moves.append(inter)
                inter = []
                
                
        return config, moves
    
    
    def FindTopOfStacks(self):
        topOfStacks = ''
        print(self.config)
        for [n,s1,s2] in self.moves:
            toMove = self.config[s1][-n:]
            self.config[s2] += toMove
            del self.config[s1][-n:]
            print(self.config)
            
        
        for crates in self.config.values():
            topOfStacks += crates[-1]
        
        
        return topOfStacks
        
        
def main():
    s = Solution('input.txt')
    
    
    
    return s.topOfStacks

if __name__ == '__main__':print(main())