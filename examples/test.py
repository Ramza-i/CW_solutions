def f(x):
    return 10 / x


if __name__ == '__main__':
    try:
        print(f('z'))
    except ZeroDivisionError:
        print('zero division')
    except TypeError:
        print('type error')



