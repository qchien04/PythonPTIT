
def cut(arr):
    minNum=1e18;
    finalNum=""
    for num in arr:
        if(num.isdigit()): finalNum=finalNum+num
        else:
            if(len(finalNum)>0):
                minNum=min(minNum,int(finalNum))
            finalNum=""
    if(len(finalNum)>0):
        minNum=min(minNum,int(finalNum))
    return minNum
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        a=list(input())
        print(cut(a))