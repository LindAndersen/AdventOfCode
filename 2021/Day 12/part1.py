import numpy as np

class Solution:
    def __init__(self,filename):
        self.crudeArr= np.loadtxt(filename, dtype=object)
        for i, elm in list(enumerate(self.crudeArr)):
            values = elm.split('-')
            self.crudeArr[i] = (values[0],values[1])
        self.pathDict = self.BuildPath()
        self.validPaths = []
        self.DFS()
        
    def __repr__(self):
        representation = (
                        f'Input:\n{self.crudeArr}\n\n'
                        f'Path Dictionary: \n{self.pathDict}\n\n'
                        f'All valid paths:\n'
            )
        if self.validPaths != None:
            for i, line in enumerate(self.validPaths):
                representation += f'\nNo. {i+1} - {line}'
        else:
            representation += f'\nNone'
        
        return str(representation)
    
    
    
    def BuildPath(self):
        pathDict = {}
        
        for i,j in self.crudeArr:
            if i in pathDict.keys() and j != 'start':
                pathDict[i].append(j)
            elif j != 'start':
                pathDict[i] = [j]
            if j in pathDict.keys() and i != 'start':
                pathDict[j].append(i)
            elif i != 'start':
                pathDict[j] = [i]
        
        del pathDict['end']
        
        return pathDict
        
    
    def DFS(self, cave='start', smallCavesVisited=[], path=[]):
        if cave in smallCavesVisited:
            return
        elif cave == 'end':
            path.append(cave)
            self.validPaths.append(path)
            return
        elif cave.islower():
            smallCavesVisited.append(cave)
            
        path.append(cave)
        
        for nextt in self.pathDict[cave]:
            print(nextt)
            self.DFS(nextt, smallCavesVisited, path)
            
    

    
def main():
    #s = Solution('input.txt')
    s = Solution('smallExample.txt')
    print(f'{s}\n')
    


if __name__ == '__main__':main()