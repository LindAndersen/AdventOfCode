#CO2 Scrubber rating, least common

data = open('input.txt','r')
inp = [x.strip() for x in data]
data.close()

#inp = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

counter = 0
check = []
delete = []

while len(inp) != 1:
    for i in inp:
        check.append(i[counter])
    if check.count('1') > check.count('0'):
        for x in range(len(check)):
            if check[x] == '1':
                delete.append(x)
    elif check.count('1') == check.count('0'):
        for x in range(len(check)):
            if check[x] == '1':
                delete.append(x)
    else:
        for x in range(len(check)):
            if check[x] == '0':
                delete.append(x)
                
    for index in sorted(delete, reverse=True):
        del inp[index]
        
    check = []
    delete = []
    counter += 1
    
    print('Iterations: {} \nLength of input: {}'.format(counter,len(inp)))

print(inp[0])
print(int((inp[0]),2))