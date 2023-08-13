import math as m
import numpy as np
import copy
from sympy import Eq


class Solution:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            path1, path2 = [path.split(',') for path in file.read().rstrip('\n').split('\n')]
        self.path1 = self.PathReader(path1)
        self.path2 = self.PathReader(path2)
        self.part1 = self.solvePart1()
        self.part2 = self.solvePart2()
    
    def AbsoluteVector(self, position, vector):
        return [position[0]+vector[0], position[1]+vector[1]]


    def PathReader(self, path):
        readPath = []
        currentPos = [0,0]
        for move in path:
            direction, length = move[0], int(move[1:])
            vector = [0,0]
            beforePos = copy.deepcopy(currentPos)

            if direction == 'U':
                currentPos[1] += length
                vector[1] += length
            elif direction == 'D':
                currentPos[1] -= length
                vector[1] -= length
            elif direction == 'L':
                currentPos[0] -= length
                vector[0] -= length
            elif direction == 'R':
                currentPos[0] += length
                vector[0] += length

            readPath.append((beforePos,vector))

        return readPath
    
    def DotProduct(self, v1, v2):
        return v1[0]*v2[0]+v1[1]*v2[1]
    
    def VectorSolve(self, v1, v2):
        pass

    def solvePart1(self):
        crossovers = []

        for (p1, v1) in self.path1:
            for (p2, v2) in self.path2:
                if self.DotProduct(v1, v2) == 0:
                    print('found cross')
                    #solve equation to get point
                    crossovers.append(None)


        return None



        
    
    def solvePart2(self):
        pass

    
    def PrintSolution(self):
        print(f'Solution for part 1: {self.part1}')
        print(f'Solution for part 2: {self.part2}')
    
def main(filename):
    s = Solution(filename)
    s.PrintSolution()



if __name__ == '__main__':main('input_files/day3.txt')