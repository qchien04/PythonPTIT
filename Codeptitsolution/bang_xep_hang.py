arr=[]
for _ in range(int(input())):
    t=["",0,0]
    name=input()
    a,b=map(int,input().split())
    t[0]=name
    t[1]=a
    t[2]=b
    arr.append(t)

arr=sorted(arr,key=lambda x:(-x[1],x[2],x[0]))

for i in arr:
    print(i[0],i[1],i[2])