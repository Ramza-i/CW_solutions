def parse_int(string):
    num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
           'eight': 8, 'nine': 9, 'ten': 10,
           'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
           'eighteen': 18, 'nineteen': 19, 'twenty': 20,
           'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
           'hundred': 100}

    s = string.lower().replace(' and', '').replace('-', ' ')
    if 'million' in s:
        return num.get(s.split()[0]) * 1_000_000
    if 'thousand' in s:
        s = s.split(' thousand')
        for i in range(len(s)):
            s[i] = [num.get(x) for x in s[i].split()]
            for j, item in enumerate(s[i]):
                if item is None:
                    return sum(s[0]) * 1000
                if item == 100:
                    s[i][j - 1] = s[i][j - 1] * 100
                    s[i][j] = 0
        return sum(s[0]) * 1000 + sum(s[1])
    s = [num.get(x) for x in s.split()]
    if len(s) == 1:
        return s[0]
    for j, item in enumerate(s):
        if item == 100:
            s[j - 1] *= 100
            s[j] = 0
    return sum(s)

print(parse_int("seven hundRED eighty-three thousand nine hundred And nineteen"))
print(parse_int("seven hundRED thousand nine hundred And nineteen"))
print(parse_int("one"))
print(parse_int("one hundred"))
print(parse_int('two thousand'))
print(parse_int('one hundred thousand'))
print(parse_int('two million'))
# print(parse_int('zero'))

# ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
#         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
#         'eighteen', 'nineteen']
# TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#
# def parse_int(string):
#     print(string)
#     numbers = []
#     for token in string.replace('-', ' ').split(' '):
#         if token in ONES:
#             numbers.append(ONES.index(token))
#         elif token in TENS:
#             numbers.append((TENS.index(token) + 2) * 10)
#         elif token == 'hundred':
#             numbers[-1] *= 100
#         elif token == 'thousand':
#             numbers = [x * 1000 for x in numbers]
#         elif token == 'million':
#             numbers = [x * 1000000 for x in numbers]
#     return sum(numbers)