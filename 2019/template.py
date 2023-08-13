class Solution:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            input = list(map(int,file.read().rstrip('\n').split(',')))
        self.input = input
        self.part1 = self.solvePart1()
        self.part2 = self.solvePart2()
    
    def solvePart1(self):
        pass
    
    def solvePart2(self):
        pass

    
    def PrintPart1(self):
        print(f'Solution for part 1: {self.part1}')

    def PrintPart2(self):
        print(f'Solution for part 2: {self.part2}')
    
def main(filename):
    s = Solution(filename).PrintPart1()
    s = Solution(filename).PrintPart2()


if __name__ == '__main__':main('input_files/day2.txt')