import itertools
from art import tprint


class Card:
    def __init__(self, input_: str):
        self.card_ = input_
        self.rank = self.get_rank(input_)
        self.suit = input_[-1]

    def __repr__(self):
        return f'{self.card_}'

    def __gt__(self, other):
        return self.rank > other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def get_rank(self, card):
        rank_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                     'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return rank_dict.get(card[:-1])


class Combination:

    def __init__(self, list_of_cards):
        self.cards_ = sorted([Card(x) for x in list_of_cards], reverse=True)

    def __repr__(self):
        return f'{self.cards_}'

    def get_pool(self):
        return list(itertools.combinations(self.cards_, 5))

    def isStraightFlush(self, arr):
        return self.isFlush(arr) and self.isStraight(arr)

    def isFlush(self, arr):
        return len(set([x.suit for x in arr])) == 1

    def isStraight(self, arr):
        for i in range(len(arr) - 1):
            if arr[i].rank - 1 != arr[i + 1].rank:
                return False
        return True

    def isFour(self, arr):
        for i in set([x.rank for x in arr]):
            if [x.rank for x in arr].count(i) == 4:
                return True
        return False

    def isSet(self, arr):
        for i in set([x.rank for x in arr]):
            if [x.rank for x in arr].count(i) == 3:
                return True
        return False

    def isPair(self, arr):
        for i in set([x.rank for x in arr]):
            if [x.rank for x in arr].count(i) == 2:
                return True
        return False

    def isFullHouse(self, arr):
        tmp = sorted([x.card_[0] for x in arr], reverse=True,
                     key=lambda x: [x.card_[0] for x in arr].count(x))
        if tmp[0] == tmp[1] == tmp[2] and tmp[3] == tmp[4]:
            return True
        return False

    def isTwoPair(self, arr):
        tmp = sorted([x.card_[0] for x in arr], reverse=True,
                     key=lambda x: [x.card_[0] for x in arr].count(x))
        if tmp[0] == tmp[1] and tmp[2] == tmp[3]:
            return True
        return False

    def best_hand(self):
        for combination in self.get_pool():
            if self.isStraightFlush(combination):
                return "straight-flush", self.get_out(combination)
        for combination in self.get_pool():
            if self.isFour(combination):
                return 'four-of-a-kind', self.get_out(combination)
        for combination in self.get_pool():
            if self.isFullHouse(combination):
                return 'full house', self.get_out(combination)
        for combination in self.get_pool():
            if self.isFlush(combination):
                return 'flush', self.get_out(combination)
        for combination in self.get_pool():
            if self.isStraight(combination):
                return 'straight', self.get_out(combination)
        for combination in self.get_pool():
            if self.isSet(combination):
                return 'three-of-a-kind', self.get_out(combination)
        for combination in self.get_pool():
            if self.isTwoPair(combination):
                return 'two pair', self.get_out(combination)
        for combination in self.get_pool():
            if self.isPair(combination):
                return 'pair', self.get_out(combination)
        return 'nothing', [x.card_[:-1] for x in self.get_pool()[0]]

    def get_out(self, combination):
        out = [j.card_[:-1] for j in
               sorted(combination, reverse=True, key=lambda x: [card.rank for card in combination].count(x.rank))]
        res = []
        for i in out:
            if i not in res:
                res.append(i)
        return res


def hend(hend, community):
    c = Combination(hend + community)
    return c.best_hand()
# if __name__ == '__main__':

# tprint("OHO      PAbOTAET")
