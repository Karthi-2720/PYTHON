def hello(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(hello(1,2,3,4,5))