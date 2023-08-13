import math as m
import copy


class Solution:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            input = list(map(int,file.read().rstrip('\n').split(',')))
        self.input = input
        self.inputCopy = copy.deepcopy(input)
        self.part1 = self.solvePart1(12, 2)
        self.part2 = self.solvePart2()
    
    def solvePart1(self, address1, address2):
        pointer = 0
        running = True

        self.input[1] = address1
        self.input[2] = address2

        while running:
            opcode = self.input[pointer]
            #print(f'Pointer -> {pointer}\nOpcode -> {opcode}')
            #print(self.input)
            if opcode == 1:
                self.input[self.input[pointer+3]] = self.input[self.input[pointer+1]] + self.input[self.input[pointer+2]]
            elif opcode == 2:
                self.input[self.input[pointer+3]] = self.input[self.input[pointer+1]] * self.input[self.input[pointer+2]]
            elif opcode == 99:
                running = False
            else:
                print(f'ERROR Opcode -> {opcode}')
                running = False
            pointer += 4

        result = self.input[0]
        self.input = copy.deepcopy(self.inputCopy)

        return result
    
    def solvePart2(self):
        for address1 in range(0,100):
            for address2 in range(0,100):
                if self.solvePart1(address1, address2) == 19690720:
                    return 100*address1+address2

    
    def PrintPart1(self):
        print(f'Solution for part 1: {self.part1}')

    def PrintPart2(self):
        print(f'Solution for part 2: {self.part2}')
    
def main(filename):
    s = Solution(filename).PrintPart1()
    s = Solution(filename).PrintPart2()


if __name__ == '__main__':main('input_files/day2.txt')