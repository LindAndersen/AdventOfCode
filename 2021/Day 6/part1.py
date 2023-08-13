import numpy as np

class Lanternfish:
    all_fish = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
    
    def __init__(*args):
        if len(args) != 0:
            Lanternfish.all_fish[str(args[0])] += 1
        else:
            Lanternfish.all_fish['9'] += 1
            
def get_inp():
    with open('input.txt','r') as inp:
        fish = ''
        for i in inp:
            fish += i
            
    inp = np.fromstring(fish, dtype=int, sep=',')
        
    return inp 
    
    
def main():
    start = get_inp()
    #start = np.array([3,4,3,1,2])
    for f in start:
        Lanternfish.all_fish[str(f)] += 1
    
    print(Lanternfish.all_fish)
    
    for i in range(256):
        to_spawn = Lanternfish.all_fish['0']
        for key, value in Lanternfish.all_fish.items():
            if key == '0': continue
            key = int(key) - 1
            Lanternfish.all_fish[str(key)] = value
        Lanternfish.all_fish['8'] = to_spawn
        Lanternfish.all_fish['6'] += to_spawn
            
        
        
        
    return print(sum(Lanternfish.all_fish.values()))
                
    
    
    
if __name__ == '__main__': main()