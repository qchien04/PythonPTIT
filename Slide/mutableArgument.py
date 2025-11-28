def myFunc(x):
    for i, c in enumerate(x):
        x[i] = 'x'
    print('Inside: {}'.format(x))
    return

x = [0, 1, 2, 3, 4]
print('before: {}'.format(x))
myFunc(x)
print('after : {}'.format(x))

####################################
# def myFunc(x):
#     x = 6886
#     print('Inside: {}'.format(x))
#     return

# x = 'Xin Chao'
# print('before: {}'.format(x))
# myFunc(x)
# print('after : {}'.format(x))