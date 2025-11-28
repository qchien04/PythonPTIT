# def myFunc(x, y, N = 10, M = 'Something' ):
#     print('positional arguments: {}, {}'.format(x, y))
#     print('Keyword    Arguments: {}, {}'.format(N, M))
#     return

# #myFunc(1, 'An Argument')
# myFunc(1, 'An Argument', N = 100, M = 'SomeWhere')

##########################################################
# def myFunc(*arg, **kwargs):
#     for i, pos in enumerate(arg):
#         print('position {} argument: {}'.format(i, pos))
#     for kw in kwargs:
#         print('keyword: {} argument: {}'.format(kw, kwargs[kw]))
#     return

#myFunc(1, 'A Pos Argument')
#myFunc(1, 'A Pos Argument', N = 100, M = 'SomeWhere')
# arg = (1, 'A Pos Argument')
# kwArg = {'N':999, 'M': 'Sometime'}
# myFunc(*arg, **kwArg)
