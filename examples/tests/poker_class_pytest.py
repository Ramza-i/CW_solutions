import pytest

from examples.poker_class import *


def test_StreetFlush():
    assert hend(['K♠', 'A♠'], ['Q♠', '5♦', '10♠', 'J♠', '8♦']) == ('straight-flush', ['A', 'K', 'Q', 'J', '10'])


def test_four1():
    assert hend(['K♠', 'J♠'], ['K♣', 'K♦', '9♦', 'K♥', '8♦']) == ('four-of-a-kind', ['K', 'J'])


def test_four2():
    assert hend(['9♠', '4♠'], ['9♣', '9♦', 'K♦', '9♥', '8♦']) == ('four-of-a-kind', ['9', 'K'])


def test_fullhouse1():
    assert hend(['K♠', '4♠'], ['K♣', 'K♦', '9♦', '8♥', '8♦']) == ('full house', ['K', '8'])


def test_fullhouse2():
    assert hend(['K♠', '4♠'], ['8♣', 'K♦', '9♦', '8♥', '8♦']) == ('full house', ['8', 'K'])


def test_flush1():
    assert hend(['K♠', '4♠'], ['8♠', 'K♦', '9♠', '8♥', '7♠']) == ('flush', ['K', '9', '8', '7', '4'])


def test_flush2():
    assert hend(['K♠', '4♠'], ['8♠', 'K♦', '9♠', 'J♥', '7♠']) == ('flush', ['K', '9', '8', '7', '4'])


def test_strraight1():
    assert hend(['A♣', '10♠'], ['8♠', 'Q♦', '9♠', 'J♣', '7♠']) == ('straight', ['Q', 'J', '10', '9', '8'])


def test_strraight2():
    assert hend(['A♣', '10♠'], ['8♠', 'Q♦', '9♠', 'J♣', 'K♠']) == ('straight', ['A', 'K', 'Q', 'J', '10'])


def test_strraight3():
    assert hend(['6♣', '10♠'], ['2♠', '3♦', '4♠', 'J♣', '5♠']) == ('straight', ['6', '5', '4', '3', '2'])


def test_set1():
    assert hend(['6♣', '10♠'], ['2♠', '6♦', '6♠', 'J♣', '5♠']) == ('three-of-a-kind', ['6', 'J', '10'])


def test_set2():
    assert hend(['2♣', '9♠'], ['2♠', '2♦', '4♠', 'Q♣', '5♠']) == ('three-of-a-kind', ['2', 'Q', '9'])


def test_twopair1():
    assert hend(['2♣', '9♠'], ['2♠', '4♦', '4♠', 'Q♣', '5♠']) == ('two pair', ['4', '2', 'Q'])


def test_twopair2():
    assert hend(['2♣', 'Q♠'], ['5♠', '2♦', '4♠', 'Q♣', '5♠']) == ('two pair', ['Q', '5', '4'])


def test_pair1():
    assert hend(['2♣', 'Q♠'], ['3♠', '2♦', '4♠', 'J♣', '5♠']) == ('pair', ['2', 'Q', 'J', '5'])


def test_pair2():
    assert hend(['2♣', 'Q♠'], ['3♠', '7♦', '4♠', 'Q♣', '6♠']) == ('pair', ['Q', '7', '6', '4'])


#
def test_nothing1():
    assert hend(['A♣', '9♠'], ['3♠', '7♦', '4♠', 'Q♣', 'K♠']) == ('nothing', ['A', 'K', 'Q', '9', '7'])


def test_nothing2():
    assert hend(['2♣', 'Q♠'], ['3♠', '7♦', '4♠', '10♣', '6♠']) == ('nothing', ['Q', '10', '7', '6', '4'])


def test_dop1():
    assert hend(['K♠', 'J♠'], ['Q♠', '10♠', '9♦', 'A♠', 'J♠']) == ('straight-flush', ['A', 'K', 'Q', 'J', '10'])


def test_dop2():
    assert hend(['K♠', 'J♥'], ['Q♦', '10♦', '9♦', 'A♠', 'Q♣']) == ('straight', ['A', 'K', 'Q', 'J', '10'])


def test_dop3():
    assert hend(['K♠', 'J♥'], ['5♦', 'K♦', '9♦', 'A♠', 'Q♣']) == ('pair', ['K', 'A', 'Q', 'J'])


if __name__ == '__main__':
    pytest.main()
