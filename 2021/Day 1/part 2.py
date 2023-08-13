data = open('day1.txt','r')
inp = [int(x) for x in data]
data.close()

n = 0
for i in range(len(inp)-3):
    SW1 = inp[i]+inp[i+1]+inp[i+2]
    SW2 = inp[i+1]+inp[i+2]+inp[i+3]
    if SW1 < SW2:
        n += 1
        
print(n)
        

        