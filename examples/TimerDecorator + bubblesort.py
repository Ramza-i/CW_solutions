import random, time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print('\r', end='')
        print(f'Время выполения - {time.time() - start}')
        return result

    return wrapper


@timer
def bubble(arr: list) -> list:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print('\r', end='')
                print(arr, end='')
                time.sleep(0.5)
    return arr


# print(bubble([random.randint(0, 10) for i in range(10)]))
a = [i for i in range(1000)]
print(a)
random.shuffle(a)
print(a)
