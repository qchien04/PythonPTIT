def kt(s1,s2):
    a=[0]*100
    b=[0]*100
    for i in s1:
        a[ord(i)-ord("a")]+=1
    for i in s2:
        b[ord(i)-ord("a")]+=1
    for i in range(29):
        if a[i]!=b[i]: return "NO"
    return "YES"
for i in range(int(input())):
    s1=input()
    s2=input()
    print("Test ",i+1,": ",kt(s1,s2),sep="")
    
        
