# two approaches to finding minimum number, explaning big-O notation
# first function is n^2
# second function is n (linear)
import time
from random import randrange

def findMin(alist):
    overallMin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin

def findMinimum(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar
# print(findMin([5,4,2,1,0]))

for listSize in range(1000, 10001, 1000):
    alist = [randrange(1000000) for x in range(listSize)]
    start = time.time()
    print(findMinimum(alist))
    end = time.time()
    print("size %d time: %f" % (listSize, end - start) )
