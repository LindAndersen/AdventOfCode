import numpy as np

class Solution:
    def __init__(self, filename):
        self.grid = self.ReadData(filename)
        self.visibleTrees = self.GetVisibleTrees()
        self.viewingScore = self.GetViewingScore()
        
        
        
    def ReadData(self, filename):
        data = []
        with open(filename,'r') as f:
            for line in f:
                data.append([int(tree) for tree in line.strip()])
                
        return data
    
    
    def IsVerticalCovered(self, tree, x, y):
        above = False
        below = False
        
        for index, line in enumerate(self.grid):
            if line[y] >= tree and index < x:
                above = True
            elif line[y] >= tree and index > x:
                below = True
                
        return above and below
                
    
    
    def IsHorizontalCovered(self, tree, x, y):
        left, right = False, False
        horzLeft, horzRight = self.grid[x][:y], self.grid[x][y+1:]
        
        for t in horzLeft:
            if t >= tree:
                left = True
                break
            
        for t in horzRight:
            if t >= tree:
                right = True
                break
        
        return left and right
    
    
    def XShapeIsCovered(self, tree, x, y):
        v = self.IsVerticalCovered(tree, x, y)
        h = self.IsHorizontalCovered(tree, x, y)
        
        
        return h and v 
    
        
    
    def GetVisibleTrees(self):
        visibleTrees = 0
        
        for x, horzTrees in enumerate(self.grid):
            for y, tree in enumerate(horzTrees):
                if x == 0 or y == 0 or y == len(horzTrees)-1 or x == len(self.grid)-1:
                    #print(f'Found an edge: {tree} @ ({x},{y})')
                    visibleTrees += 1
                elif not self.XShapeIsCovered(tree, x, y):
                    #print(f'Found a visible tree: {tree} @ ({x},{y})')
                    visibleTrees += 1
                    
                    
        return visibleTrees
    
    
    def FindViewingDistance(self, tree, listOfTrees):
        score = 0
        print(listOfTrees)
        if len(listOfTrees) == 0:
            return score
        
        for i in listOfTrees:
            if i < tree:
                score += 1
            else:
                break
            
        return score
        
    
    def GetHorzScore(self, tree, x, y, grid):
        leftTrees = grid[x][:y]
        rightTrees = grid[x][y+1:]
        
        return self.FindViewingDistance(tree, leftTrees)*self.FindViewingDistance(tree, rightTrees)
    
    
    def GetVertScore(self, tree, x, y):
        transposed = np.array(self.grid).T.tolist()
        
        return self.GetHorzScore(tree, x, y, transposed)
        
        
    
    def GetViewingScore(self):
        allScores = []
        
        for x, line in enumerate(self.grid):
            for y, tree in enumerate(line):
                horzScore = self.GetHorzScore(tree, x, y, self.grid)
                vertScore = self.GetVertScore(tree, x, y)
                score = horzScore*vertScore
                allScores.append(score)
        
        print(allScores)
        
        return sorted(allScores)[-1]
    
    
    
    
    
    
    
    
def main():
    #s = Solution('input.txt')
    s = Solution('example.txt')
    print(f'Part 1: {s.visibleTrees}')
    print(f'Part 2: {s.viewingScore}')
    
    return s.visibleTrees


if __name__ == '__main__': main()