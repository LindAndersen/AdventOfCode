class Node:
    def __init__(self, name, children=[], size=0, parent=None, depth=0):
        self.name = name
        self.children = children
        self.size = size
        self.parent = parent
        self.depth = depth
    
    
    def __repr__(self):
        return f'{self.name}'
            


class Solution:
    def __init__(self,filename):
        self.data = self.ReadData(filename)
        self.root = self.MakeFileSystem()
        
    def printTree(self):
        for a in self.root.children:
            print(a)
            for b in a.children:
                print(b)
                for c in b.children:
                    print(c)
                    for d in c.children:
                        print(d)
        
    def ReadData(self, filename):
        with open(filename,'r') as f:
            data = [line.split() for line in f]
            
        return data[1:]
    
    def GetCommandFromInput(self, command, root, node):
        if len(command) == 1:
            return node
        
        if command[0] == 'cd':
            if command[1] == '..':
                currentNode = node.parent
            elif command[1] == '/':
                currentNode = root
            else:
                #checkChildren = [c.name for c in node.children]
                #if command[1] in checkChildren:
               #     return node.children[checkChildren.index(command[1])]
                node.children.append(Node(command[1], parent=node, depth=node.depth+1))
                currentNode = node.children[-1]
                
        
        return currentNode
        
    def MakeFileSystem(self):
        root = Node('/')
        currentNode = root
        
        for line in self.data:
            if line[0] == '$':
                currentNode = self.GetCommandFromInput(line[1:], root, currentNode)
            elif line [0] == 'dir':
                currentNode.children.append(Node(line[1], parent=currentNode, depth=currentNode.depth+1))
            else:
                currentNode.children.append(Node(line[1],size=line[0],parent=currentNode, depth=currentNode.depth+1))
                
                
        return root
    
    def FindSize(self):
        currentNode = self.root
        sizeSum = 0
        childWithChildrensIndex = []
        hasChildren = True
        
        while hasChildren:
            for child in currentNode.children:
                if child.size == 0:
                    childWithChildrensIndex.append(currentNode.children.index(child))
                sizeSum += child.size
            
            if len(childWithChildrensIndex) == 0:
                currentNode.size = sizeSum
                sizeSum = 0
                hasChildren = False
                
            currentNode = currentNode.children[childWithChildrensIndex[0]]
            
            
            
                
        
        
def main():
    s = Solution('input.txt')
    
    
    return s.printTree()
    
if __name__ == '__main__': main()