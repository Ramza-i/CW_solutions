def productFib(prod):
    f = [0,1]
    i=0
    while f[i]*f[i+1]<=prod:
        f.append(f[i]+f[i+1])
        i += 1
    return [f[-3],f[-2], True] if f[-3]*f[-2] == prod else [f[-2],f[-1], False]

if __name__ == '__main__':
    print(productFib(4895))
    print(productFib(5895))