def squareGenerator(n):
    for x in range(n):
        yield x ** 2

generator = squareGenerator(10)

count = 0
while True:
    x = next(generator)
    #x = generator.__next__()
    print(count, x)
    count += 1

for count, x in enumerate(generator):
     print(count, x)

