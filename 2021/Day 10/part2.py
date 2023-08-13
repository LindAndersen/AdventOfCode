def get_inp(filename):
    outp = ''
    with open(filename,'r') as inp:
        for line in inp:
            outp += line
        
    return outp.split()       
        
        
def IllegalLine(inp):
    opensChar = ['(','<','[','{']
    reverse = {'(':')', '<':'>', '[':']', '{':'}'}
    linesToDelete = []
    correctionStrings = []
    for i, line in enumerate(inp):
        toClose = []
        for char in line:
            if len(toClose) == 0 or char in opensChar:
                toClose.append(char)
            elif char == reverse[toClose[-1]]:
                del toClose[-1]
            else:
                linesToDelete.append(i)
                break
        else:
            if len(toClose) != 0:
                correction = [reverse[x] for x in toClose[::-1]]
                correctionStrings.append(correction)
    
    linesToDelete.sort(reverse=True)
    for i in linesToDelete:
        del inp[i]
    
    
    return inp, correctionStrings

        
        
def CalcScore(correctionStrings):
    scoreDict = {')':1,']':2,'}':3,'>':4}
    scores = []
    for string in correctionStrings:
        score = 0
        for char in string:
            score *= 5
            score += scoreDict[char]
        scores.append(int(score))
   
    a, b = divmod(len(scores),2)
    finalScore = sorted(scores)[a+b-1]
    
    return finalScore
        
        
        
def main():
    inp = get_inp('input.txt')
    #inp = get_inp('test.txt')
    incompleteLines, correctionStrings = IllegalLine(inp)
    print(correctionStrings)
    score = CalcScore(correctionStrings)
    
    return score
    
    
if __name__ == '__main__': print(main())

