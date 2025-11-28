import re
import heapq
t = int(input())
for z in range(t) :
    n = int(input())
    main = ' ' + input().replace(' ', '  ') + ' '
    a = []
    i = 8
    while i > -9 and len(a)<=2:
        s = '\d' * abs(i) + ' '
        if i < 0 :
            s = '-' + s
        elif i > 0 :
            s = ' ' + s
        else :
            i -= 1
            continue
        a+=heapq.nlargest(3-len(a), re.findall(s, main))
        i -= 1
    print(int(a[0])+int(a[1])+int(a[2]))