def balanced_parens(n):
    #Рекурсивная функция
    if n == 0: return ['']
    def lec(n, cl=0, cr=0, s=''):
        if cl + cr == n*2:
            res.append(s)
        if cl < n:
            lec(n, cl+1, cr, s+'(')
        if cl > cr:
            lec(n, cl, cr+1, s+')')
        return res
    res = []
    return lec(n)
print(balanced_parens(4))



#Работает перебором 0011 0101
# def corr(s):
#     c = 0
#     for i in s:
#         if i == '(':
#             c += 1
#         if i == ')':
#             c -= 1
#             if c < 0:
#                 return False
#     if c == 0:
#         return True
#     return False

# def balanced_parens(n):
#     if n == 0:
#         return ['']
#     if n == 1:
#         return ['()']
#     res = []
#     for i in range(1,2**((n*2)-2)):
#         s = '(' + bin(i)[2:].zfill(n*2-2).replace('0','(').replace('1', ')') + ')'
#         if corr(s):
#             res.append(s)
#
#     return res
#
# print(balanced_parens(4))

