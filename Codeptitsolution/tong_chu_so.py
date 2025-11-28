s=input()
cnt=1
while len(s)>1:
    sum=0
    for i in s: 
        sum+=ord(i) - ord('0')
    s=str(sum)
    if(len(s)==1): break
    cnt+=1

print(cnt)
