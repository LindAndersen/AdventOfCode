data = open('input.txt','r')
inp = [x.split() for x in data]
data.close()

hor = 0
ver = 0

for i in range(len(inp)):
   if inp[i][0] == 'forward':
       hor += int(inp[i][1])
   elif inp[i][0] == 'down':
        ver += int(inp[i][1])
   elif inp[i][0] == 'up':
        ver -= int(inp[i][1])
        
print(hor*ver)