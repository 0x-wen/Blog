# def foo():
#     print(123)
#
# mm = lambda : print(123)
#
# mm()

ll = [1,2,3,4,5,6,7,8,9]        # [1, 2, 9,16, 25, ....]



print(list(map(lambda x: x ** 2, ll)))
