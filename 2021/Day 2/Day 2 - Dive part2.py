data = open('input.txt','r')
inp = [x.split() for x in data]
data.close()

hor = 0
ver = 0
aim = 0

print(inp)

for i in range(len(inp)):
   if inp[i][0] == 'forward':
       hor += int(inp[i][1])
       interm = aim*int(inp[i][1])
       ver += interm
   elif inp[i][0] == 'down':
        aim += int(inp[i][1])
   elif inp[i][0] == 'up':
        aim -= int(inp[i][1])
        
print(hor*ver)