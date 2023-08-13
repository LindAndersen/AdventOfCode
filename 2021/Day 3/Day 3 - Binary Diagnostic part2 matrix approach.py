data = open('input.txt','r')
inp = [x.strip() for x in data]
data.close()

inp = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']


flipinp = [x for x in inp[0][0]]

rotated_inp = [''.join(reversed(a)) for a in zip(*inp)]

print(zip(inp))