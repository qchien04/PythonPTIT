import math
def change(q):
    if q>=39: return 9.0
    if q>=37: return 8.5
    if q>=35: return 8.0
    if q>=33: return 7.5
    if q>=30: return 7.0
    if q>=27: return 6.5
    if q>=23: return 6.0
    if q>=20: return 5.5
    if q>=16: return 5.0
    if q>=13: return 4.5
    if q>=10: return 4.0
    if q>=7: return 3.5
    if q>=5: return 3.0
    return 2.5
def lamtron(q):
    if q<0.25: return 0.0
    if 0.25<=q<0.75: return 0.5
    return 1
def lamtron2(q):
    if q==0.25: return 0.5
    if q==0.75: return 1.0
    return 0.0
for _ in range(int(input())):
    inp=input().split()
    a,b=map(change,map(int,inp[0:2]))
    c,d=map(float,inp[2:])
    arr=[a,b,c,d]
    core=sum(arr)/4
    du=core-math.floor(core)
    print(f'{(math.floor(core)+lamtron(du)):.1f}')