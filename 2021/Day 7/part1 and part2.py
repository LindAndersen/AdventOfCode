import numpy as np


def get_inp():
    with open('input.txt','r') as inp:
        coords = ''
        for i in inp:
            coords += i
    coords = np.fromstring(coords, dtype=int, sep=',')
        
    return coords


def avg(coords):
    avg = round(coords.sum()/len(coords))
    return avg

def calc_fuel(coords, point):
    fuel = 0
    for coord in coords:
        fuel += abs(coord-point)
        # This is for part 2, when increasing cost for steps
        #n = abs(coord-point)
        #fuel += n * (n + 1) // 2
    return fuel

def main():
    coords = get_inp()
    fuel = 1*10**24
    for coord in range(coords.min(), coords.max()+1):
        this_fuel = calc_fuel(coords, coord)
        if fuel > this_fuel: fuel = this_fuel
            
    
    
    return fuel



if __name__ == '__main__': print(main())