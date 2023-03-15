# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
array = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

A = array
res = []
while A:
    for i in A[0]:
        res.append(i)
    A = A[1:]
    if not A:
        break
    for i in range(len(A)):
        res.append(A[i].pop(-1))
    for i in A[-1][::-1]:
        res.append(i)
    A = A[:-1]
    for i in range(len(A)-1,-1,-1):
        res.append(A[i].pop(0))

print(res)