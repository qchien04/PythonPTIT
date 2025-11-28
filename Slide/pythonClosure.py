# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function

# closure = outer_function(10)
# result = closure(5)
# print(result)

### Functions Factory ###############
# def exponentiate(power):
#     def inner(base):
#         return base ** power
#     return inner

# square = exponentiate(2)
# cube = exponentiate(3)
# print(square(2))
# print(cube(2))

### Callbacks Function
# def event_handler(event_name):
#     def callback(*args, **kwargs):
#         print(f"Event '{event_name}' triggered with: {args}, position: {kwargs}")
#     return callback

# button_click = event_handler("button_click")
# button_click("left_click", x=100, y=200)

### Data Encapsulation 
# def counter():
#     count = 0
#     def increment():
#         nonlocal count  # Use nonlocal to modify the count variable in the enclosing scope
#         count += 1
#         return count

#     def decrement():
#         nonlocal count
#         count -= 1
#         return count

#     return increment, decrement

# inc, dec = counter()  # Get closures for increment and decrement
# print(inc())
# print(inc())
# print(dec()) 