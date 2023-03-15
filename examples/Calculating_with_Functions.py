def zero(f=None): return f(0) if f is not None else 0
def one(f=None): return f(1) if f is not None else 1
def two(f=None): return f(2) if f is not None else 2
def three(f=None): return f(3) if f is not None else 3
def four(f=None): return f(4) if f is not None else 4
def five(f=None): return f(5) if f is not None else 5
def six(f=None): return f(6) if f is not None else 6
def seven(f=None): return f(7) if f is not None else 7
def eight(f=None): return f(8) if f is not None else 8
def nine(f=None): return f(9) if f is not None else 9

def plus(num): return lambda x : x + num
def minus(num): return lambda x : x - num
def times(num): return lambda x : x * num
def divided_by(num): return lambda x : x // num

if __name__ == '__main__':
    print(seven(times(five())))
    print(four(plus(nine())))
    print(eight(minus(three())))
    print(six(divided_by(two())))