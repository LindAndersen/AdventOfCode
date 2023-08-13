class Solution:
    def __init__(self,filename):
        self.data = self.ReadData(filename)
        self.endOfStartPacket = self.FindEndOfStartPacket()
        
        
    def ReadData(self,filename):
        data = ''
        
        with open(filename,'r') as f:
            for char in f:
                data += char
        
        return data
    
    
    def AllCharsUnique(self, string):
        char_set = [False] * 128
        
        for i in range(len(string)):
            val = ord(string[i])
            
            if char_set[val]:
                return False
            
            char_set[val] = True
            
        return True
    
    def FindEndOfStartPacket(self):
        windowSize = 14
        
        for i in range(windowSize-1,len(self.data)):
            window = self.data[i-windowSize+1:i+1]
            print(i)
            print(window)
            if self.AllCharsUnique(window):
                return i+1
                
    
    
        
def main():
    s = Solution('input.txt')
    
    
    
    return s.endOfStartPacket, len(s.data)

if __name__ == '__main__':print(main())