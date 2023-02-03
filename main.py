def my_get():
    for i in range(10):
        yield i, 2

aa = ( (i,i+2) for i in range(10))



print(next(aa))
print(next(aa))
print(next(aa))
print(next(aa))
