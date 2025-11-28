### Decorator
# def myDecorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @myDecorator
# def say_hello():
#     print("Hello Python")

# func = say_hello
# myDecorator(func)
# say_hello()

### Closure and Decorator
# def count_calls(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print('Call {} of {}'.format(count, func.__name__))
#         return func(*args, **kwargs)
#     return wrapper

# @count_calls
# def say_hello():
#     print("Hello!")

# for i in range(3):
#     say_hello()



### Caching
import time

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper


@memoize
def factorial(n):
    time.sleep(0.00001)
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


start_time = time.time()
factorial(300)
print((time.time() - start_time)*1000, "ms in 1st time")


start_time = time.time()
factorial(300)
print((time.time() - start_time)*1000, "ms in 2nd time")