dem3chuso , demNchuso = [0]*1001, [0]*19
for i in range(1, 1001): 
    dem3chuso[i] = dem3chuso[i-1] + ((str(i).count('6') + str(i).count('8')) if i % 8 == 0 else 0)
    
total = dem3chuso[-1]
demNchuso[3] = dem3chuso[999]

#dem so chu so 6 va 8 cua tat ca cac so co n chu so
for i in range(4, 19):
    demNchuso[i] = demNchuso[i-1] * 10 + 2 * 10**(i - 4) * 125


for t in range(int(input())):
    n = int(input())
    ans = 0
    if n<=1000: ans = dem3chuso[n]
    else: 
        n = str(n)
        m = len(n)
        pre = 0 
        for i in range(m-3):
            const = 10**(m-i-4)*125
            x = int(n[i])


            ans += x*demNchuso[m-i-1] 
            ans += pre*x*const
            if x>6: ans += const
            if x>8: ans += const


            if x==6 or x==8: pre += 1

        last = n%1000
        ans += dem3chuso[last]
        ans += pre*(1+last//8)
    print(ans)