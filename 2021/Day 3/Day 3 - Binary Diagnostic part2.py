data = open('input.txt','r')
inp = [x.strip() for x in data]
data.close()

inp = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']


def filterNumber(val, lst):
    ans = []
    for i in range(len(lst[0])):
        for j in lst:
            ans.append((j[i],lst.index(j)))
        checkDom = [item[0] for item in ans]
        
        if checkDom.count('1') == 1 or checkDom.count('0') == 1:
            return print('There was only 1 of me!!')
        
        elif checkDom.count(val)/len(lst) > 0.5:
            print('I was dominating: ' + str(val))
            for k in range(len(ans)):
                if lst[k][0] != val:
                    del lst[ans[k][1]]
        elif checkDom.count(val)/len(lst) == 0.5:
            print('We were equal!')
            for k in range(len(ans)):
                if lst[k][0] != 1:
                    del lst[ans[k][1]]
        else:
            print('I was dominating: 0')
            for k in range(len(ans)):
                if lst[k][0] == val:
                    del lst[ans[k][1]]
        ans = []
        
    return print(lst)
    
    
    
filterNumber('1',inp)