def f(x):
    return 10 // x


if __name__ == '__main__':
    try:
        print(f(2))
    except ZeroDivisionError:
        print('Zero division')
    except TypeError:
        print('Type error')
    except:
        print('Another error')



