def longestSublist(a):
    """
      Determines the longest increasing sub-list
      a -  a list of element
      return sublist of x, the longest increasing sublist

    """
    #initialise l and p
    lg = len(a)
    l = [0]*lg
    p = [0]*lg
    l[-1] = 1
    p[-1]=-1
    for k in range(lg-2, -1, -1):        
        p[k] = -1
        l[k]=1
        for i in range(k+1, lg):
            if a[i]>=a[k] and l[k]<l[i]+1:
                l[k] = l[i]+1
                p[k] = i
        print (" l =", l," p =",p)

    #identify the longest sublist
    #find the maximum length
    j = 0
    for i in range(0, lg):
        if l[i]>l[j]:
            j=i
    #collect the results using the position list
    rez = []
    while j!=-1:
        rez = rez+[a[j]]
        j = p[j]
    return rez


l = [2, 1, 9, 6, 11]
print ("    ",l)
print (longestSublist(l))