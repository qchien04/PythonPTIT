import heapq
import re

t = int(input())
for z in range(t) :
    n = int(input())
    main = ' ' + input().replace(' ', '  ') + ' '
    a = []
    i = -8
    while i < 9 and len(a) < 3:
        s = '\d' * abs(i) + ' '
        if i < 0 :
            s = '-' + s
        elif i > 0 :
            s = ' ' + s
        else :
            i += 1
            continue
        b=map(int,re.findall(s, main))
        a+=heapq.nsmallest(3-len(a), b)
        i += 1
    print(sum(a))