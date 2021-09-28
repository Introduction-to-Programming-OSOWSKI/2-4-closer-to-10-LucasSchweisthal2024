#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    10 - x
    10 - y
    if x > y:
        return x
    elif y < x:
        return y
    else:
        return "they are equal"

print(close10(9, 8))