#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    abs(10 - x)
    abs(10 - y)
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 0

print(close10(5, 18))