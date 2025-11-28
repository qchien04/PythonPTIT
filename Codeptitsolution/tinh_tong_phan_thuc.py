
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        num=int(input())
        if(num%2==0):
            res=0
            for i in range(2,num+1,2):
                res+=(1/i)
            formatted_num = "{:.6f}".format(res)
            print(formatted_num)
        if(num%2==1):
            res=0
            for i in range(1,num+1,2):
                res+=(1/i)
            formatted_num = "{:.6f}".format(res)
            print(formatted_num)