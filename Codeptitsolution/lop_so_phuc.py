import cmath
import math

t=int(input())
a=[]
while True:
    try:
        a.extend(map(int,input().split()))
    except: break

i=0
for _ in range(t):
    a1,b,c,d=a[i],a[i+1],a[i+2],a[i+3]
    i+=4
    z1=a1+b*1j
    z2=c+d*1j
    C=(z1+z2)*z1
    D=(z1+z2)**2
    print(f"{C.real:.0f} {'+' if C.imag>0 else '-'} {abs(C.imag):.0f}i, {D.real:.0f} {'+' if D.imag>0 else '-'} {abs(D.imag):.0f}i")
