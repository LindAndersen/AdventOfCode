import numpy as np

def get_inp(filename):
    outp = ''
    with open(filename,'r') as inp:
        for line in inp:
            outp += line
        
    return outp.split()       
        
        
def IllegalLine(inp):
    opensChar = ['(','<','[','{']
    reverse = {'(':')', '<':'>', '[':']', '{':'}'}
    illegalChars = []
    for line in inp:
        toClose = []
        for char in line:
            if len(toClose) == 0 or char in opensChar:
                toClose.append(char)
            elif char == reverse[toClose[-1]]:
                del toClose[-1]
            else:
                illegalChars.append(char)
                break
    
    return illegalChars
        
        
def CalcScore(illegalChars):
    scores = {')':3, ']':57, '}':1197, '>':25137}
    score = 0
    
    for char in illegalChars:
        score += scores[char]
        
    return score
        
        
        
def main():
    inp = get_inp('input.txt')
    #inp = get_inp('test.txt')
    illegalChars = IllegalLine(inp)
    print(illegalChars)
    score = CalcScore(illegalChars)
    
    
    return score
    
    
if __name__ == '__main__': print(main())