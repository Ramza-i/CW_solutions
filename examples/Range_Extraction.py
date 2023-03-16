def solution(args):
    res = [[args[0]]]
    i = 0
    out = ''
    while True:
        for num in args[1:]:
            if num == res[i][-1] + 1:
                res[i].append(num)
            else:
                i += 1
                res.append([])
                res[i].append(num)
        for i in res:
            if len(i) == 1:
                out += f'{i[0]},'
            elif len(i) == 2:
                out += f'{i[0]},{i[1]},'
            else:
                out += f'{i[0]}-{i[-1]},'

        # return f'{res} \n {out[:-1]}'
        return out[:-1]

if __name__ == '__main__':
    print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
    print(solution([-82, -80, -78, -75, -73, -72, -69, -68, -65, -62, -60, -58, -55, -53, -50, -47, -46, -45, -42, -41,
                     -40, -37, -36, -33, -32]))