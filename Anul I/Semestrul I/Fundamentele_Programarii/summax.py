'''
Created on Jan 11, 2018

@author: istvan
'''

def sumaMaxDynamic(l):
    s = [0]*len(l)
    s[-1] = l[-1]
    for i in range(len(l)-2,-1,-1):
        print(s)
        if l[i] > l[i] + s[i+1]:
            s[i] = l[i]
        else:
            s[i] = l[i] + s[i+1]
            
    return max(s)

l = [0, 2, 1, 3, 4, 5]
l=[-2, -1, -3, -4, -5]
l = [0, 2, -3, 3, 2, 5]
print(l)
print(sumaMaxDynamic(l))
