from functools import reduce
list = range(100,1001,2)
def my_list(x,y):
    return x * y
print(reduce(lambda x,y: x * y,list))
