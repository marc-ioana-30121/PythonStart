def create_cubes(n):
    result = []
    for x in range(n):
        yield x**3

for x in create_cubes(10000):
    print(x)

def gen_fion(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b, a+b

def simple_gen():
    for x in range(3):
        yield x
#problem 1
def gensquares(N):
    for x in range(N):
        yield x**2
#problem 2
import random
random.randint(1,10)

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low, high)
