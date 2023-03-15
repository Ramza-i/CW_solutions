import math, time
start = time.time()

# a = 'dhavxnqgym'
# #    myxvqnhgda
# # a = 'abcdefgjhk'
#     ekjhgfdcba
# a = '1234567890'
# #    4987653210
# #    4987653210
# a = [x for x in sorted(a)]
# #
# def find_i(arr):
#     for i in range(len(arr) - 2, -1, -1):
#         if arr[i] < arr[i + 1]:
#             return i
# def find_j(arr, i):
#     return arr.index(min([x for x in arr[i + 1:] if x > arr[i]]))
# def rev_ij(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#     return arr
#
# def rev_end(arr, i):
#     return arr[:i+1] + arr[-1:i:-1]
#
# def next(per):
#     i = find_i(per)
#     j = find_j(per,i)
#     per = rev_ij(per,i,j)
#     per = rev_end(per,i)
#     return per
# f = math.factorial(len(a))//2-1
# for i in range(f):
#     if i%10000==0:
#         print(f" to end - {f - i} {''.join(a)}")
#     a = next(a)
# print(''.join(a))
# print(time.time()-start)
#
a ='abcdefgjh'

def middle_permutation(string):
    s = [x for x in sorted(string)]
    if len(s)%2==0:
        return ''.join([s.pop(len(s)//2-1)] + s[::-1])
    return ''.join([s.pop(len(s)//2)] + [s.pop(len(s)//2-1)] + s[::-1])


print(middle_permutation(a))
print(time.time()-start)