p = { '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'T' : 10,
      'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
m = {'♠' : 0.1, '♥' : 0.2, '♣' : 0.3, '♦' : 0.4}
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def ten_to_T(a):
    return [x.replace('10', 'T') for x in a]
def T_to_ten(a):
    return [x.replace('T', '10') for x in a]

def translate(a):
    if type(a[0]) is str:
        return [p.get(x[0])+m.get(x[1]) for x in a]
    if type(a[0]) is float:
        return [get_key(p, int(x))+get_key(m, round(x%1, 1)) for x in a]
    if type(a[0]) is int:
        return [get_key(p, x) for x in a]
def result(a,b):
    return list(map(sum, zip(a,b)))
def to_out(a):
    return T_to_ten(translate(sorted(list(set(a)), reverse=True)))

def get_suit(a):
    return [round(x%1, 1) for x in a]
def get_rank(a):
    return [int(x) for x in a]
def move(a):
    return list(a[i:i+5] for i in range(3))

def isStFl(a):
    s = get_suit(a)
    r = get_rank(a)
    if len(set(s)) == 1 and isStrit(r):
            return "straight-flush", T_to_ten(translate(r))
    return False
def is4(a):
    s = get_suit(a)
    r = get_rank(a)
    count = [0]*15
    for i in r:
        count[i] +=1
    if 4 in count:
        tmp =[x[0] for x in enumerate(count) if x[1] == 4]
        return 'four-of-a-kind', T_to_ten(translate(tmp+[x for x in r if x not in tmp]))
def isFullHouse(a):
    s = get_suit(a)
    r = get_rank(a)
    c = [r.count(x) for x in r]
    if list(set(c)) == [2,3]:
        return "full house", T_to_ten(translate(sorted(list(set(r)), reverse=True)))
def isFlush(a):
    s = get_suit(a)
    r = get_rank(a)
    if len(set(s)) == 1:
        return "flush", T_to_ten(translate(sorted(list(set(r)), reverse=True)))
def isStrit(a):
    s = get_suit(a)
    r = get_rank(a)
    if all(r[i]-1 == r[i+1] for i in range(len(r)-1)):
        return "straight", T_to_ten(translate(sorted(list(set(r)), reverse=True)))
def is3(a):
    r = get_rank(a)
    count = [0] * 15
    for i in r:
        count[i] += 1
    if 3 in count:
        return 'three-of-a-kind', T_to_ten(translate(sorted(list(set([x[0] for x in enumerate(count) if x[1] == 3] + r)), reverse=True)))
def isTwoPair(a):
    r = get_rank(a)
    count = [0]*15
    for i in r:
        count[i] +=1
    if len([x[0] for x in enumerate(count) if x[1] == 2]) == 2:
        return 'two pair',T_to_ten(translate(sorted(list(set([x[0] for x in enumerate(count) if x[1] == 2]+r)), reverse=True)))
def isPair(a):
    r = get_rank(a)
    count = [0]*15
    for i in r:
        count[i] +=1
    if 2 in count:
        tmp = list(set([x[0] for x in enumerate(count) if x[1] == 2]))
        return 'pair', T_to_ten(translate(tmp + [x for x in r if x not in tmp]))

def isNothing(a):
    s = get_suit(a)
    r = get_rank(a)
    return "nothing", T_to_ten(translate(sorted(list(set(r)), reverse=True)))

def hand(hole_cards, community_cards):
    s = ten_to_T(community_cards) + ten_to_T(hole_cards)
    s = sorted(translate(s), reverse=True)

    for i in move(s):
        if isStFl(i):
            return isStFl(i)
    for i in move(s):
        if is4(i):
            return is4(i)
    for i in move(s):
        if isFullHouse(i):
            return isFullHouse(i)
    for i in move(s):
        if isFlush(i):
            return isFlush(i)
    for i in move(s):
        if isStrit(i):
            return isStrit(i)
    for i in move(s):
        if is3(i):
            return is3(i)
    for i in move(s):
        if isTwoPair(i):
            return isTwoPair(i)
    for i in move(s):
        if isPair(i):
            return isPair(i)
    return isNothing(move(s)[0])