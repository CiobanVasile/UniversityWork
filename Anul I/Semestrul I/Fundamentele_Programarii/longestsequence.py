def longestSequence(l):
    """
      Compute the longest increasing sequence
      l - list of elements
      return list - longest increasing sequence
    """
    lgs = [0]*len(l)
    #the longest sequence starting from
    #the last element is 1
    lgs[len(l)-1] = 1
    for k in range(len(l)-2,-1,-1):
        print (lgs)
        if l[k+1]>=l[k]:
            #if is increasing
            lgs[k]=lgs[k+1]+1
        else:
            lgs[k] = 1 #start a new sequence
    #find the longest
    maxLg = 1
    pozMax = len(l)-1
    for i in range(0,len(lgs)):
        if lgs[i]>maxLg:
            maxLg = lgs[i]
            pozMax = i
    return l[pozMax:pozMax+maxLg]

l = [1,2,3,1,2,3,4,1]
print(l)
print (longestSequence(l))
