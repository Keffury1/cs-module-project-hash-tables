import random
import math

my_dict = {}

def slowfun(x,y):
    key = (x,y)

    if key not in my_dict:
        v = math.pow(x,y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        my_dict[key] = v
    return my_dict[key]

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
