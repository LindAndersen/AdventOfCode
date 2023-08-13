data = open('input.txt','r')
inp = [x.strip() for x in data]
data.close()

#inp = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

ans = []
gamma = ''
epsi = ''
for i in range(len(inp[0])):
    for j in inp:
        ans.append(j[i])
    #print(ans.count('1'), ans.count('0'))
    if ans.count('1') > ans.count('0'):
        gamma += '1'
        epsi += '0'
    else:
        gamma += '0'
        epsi += '1'
    ans = []


#print(gamma, epsi)
print(int(gamma,2)*int(epsi,2))