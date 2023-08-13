import numpy as np

class Solution:
    def __init__(self, filename, dtype=int):
        self.filename = filename
        
    def SumOfXMostCalories(self, n):
        caloriesSums = []
        with open(self.filename,'r') as file:
            inter = []
            for line in file:
                if line == '\n':
                    caloriesSums.append(sum(inter))
                    inter = []
                    continue
                inter.append(int(line.strip()))
        caloriesSums.sort(reverse=True)
        
        return sum(caloriesSums[0:n])
        
        

def main():
    s = Solution('input.txt')
    ans = s.SumOfXMostCalories(3)
    
    return ans

if __name__ == '__main__': print(main())