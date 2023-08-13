import math as m


class Solution:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            input = [int(fuel.strip()) for fuel in file]
        self.input = input
        self.totalFuel = self.CalcTotalFuel()
        self.totalFuelActually = self.CalcTotalFuelActually()

    def FuelFromMass(self, mass):
        fuel = m.floor(mass/3) - 2

        return fuel
    
    def CalcTotalFuel(self):
        fuel = 0
        for mass in self.input:
            fuel += self.FuelFromMass(mass)

        return fuel
    
    def CalcTotalFuelActually(self):
        fuel = 0
        for mass in self.input:
            moduleFuel = self.FuelFromMass(mass)
            fuel += moduleFuel
            while moduleFuel > 0:
                moduleFuel = self.FuelFromMass(moduleFuel)
                if moduleFuel > 0:
                    fuel += moduleFuel

        return fuel
    
    def PrintPart1(self):
        print(f'Solution for part 1: {self.totalFuel}')

    def PrintPart2(self):
        print(f'Solution for part 2: {self.totalFuelActually}')
    
def main(filename):
    #s = Solution(filename).PrintPart1()
    s = Solution(filename).PrintPart2()


if __name__ == '__main__':main('input_files/day1.txt')