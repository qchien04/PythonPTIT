# def solve(f):
#     with open(f, 'r') as file:
#         arr = set()
#         for line in file:
#             email = line.strip().lower()
#             arr.add(email)
    
#     arr = sorted(arr)
    
#     for i in arr:
#         print(i)

# if __name__ == "__main__":
#     solve('CONTACT.in')

se=set()
with open("CONTACT.in", 'r') as file:
    while True:
        try:
            s=input().strip()
            se.add(s.lower())
        except Exception as e:
            break
    a=sorted(se)
    for i in a:
        print(i)
