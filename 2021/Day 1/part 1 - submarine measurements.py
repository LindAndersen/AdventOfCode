data = open('day1.txt','r')
inp = [int(x) for x in data]
data.close()

print(divmod(len(inp),3))

n = 0
for i in range(1,len(inp)):
    if inp[i] > inp[i-1]:
        n += 1
        
print(n)
        

        