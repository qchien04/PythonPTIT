def div(i):
    return int(i)%42
if __name__ == '__main__':
    a=set()
    while True:
        try:
            s=input()
        except EOFError:
             break
        b=list(map(div,s.split()))
        a.update(b)
    print(len(a))         