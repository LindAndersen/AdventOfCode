import numpy as np

class Solution:
    def __init__(self, filename):
        self.inp = np.loadtxt(filename, dtype=object)
        
        
        
        
        
        
        
        
def main():
    s = Solution('input.txt')
    
    return s.inp

if __name__ == '__main__': print(main())