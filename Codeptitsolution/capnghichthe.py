


n=int(input())
arr=list(map(int,input().split()))
cnt=0
for index,val in enumerate(arr):
    for j in range(index+1,len(arr)):
        if(val>arr[j]):
            cnt+=1
print(cnt)