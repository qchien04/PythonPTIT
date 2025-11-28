# for i in range(int(input())):
#     a,b=map(int,input().split())
#     ans=0
#     for i in range(b,a+1,b):
#         while(i%b==0):
#             ans+=1
#             i/=b
#     print(ans)


for _ in range(int(input())):
    cnt=0
    n,p=map(int,input().split())
    for i in range(1,n+1):
        while(i%p==0):
            cnt+=1
            i/=p
    print(cnt)