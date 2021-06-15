# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart
# or diamond.
#
# The itertools library may be helpful. Feel free to
# define multiple functions if it helps you solve the
# problem.

import itertools

# ----------------------------------------------------------------------------
# MINHA SOLUÇÃO (funções best_wild_hand, jokers2, combs)
# ----------------------------------------------------------------------------


def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."

    wildhands = jokers2(hand)
    hands = []

    for h in wildhands:
        hands_of5 = itertools.combinations(h, 5)
        hands.extend(hands_of5)
        cu = [list(u) for u in hands]

    # cu é todas as listas de 5 mãos possíveis
    return max(cu, key=hand_rank)


def jokers2(the_hand):

    reds = [r + s for r in '23456789TJQKA' for s in 'DH']
    blax = [r + s for r in '23456789TJQKA' for s in 'SC']
    hand = the_hand[:]
    hands = []

    if '?R' in hand and '?B' in hand:
        hand.remove('?R')
        hand.remove('?B')
        wild = [[r, s] for r in reds for s in blax]
        hands = combs(hand, wild)

    elif '?R' in hand:
        hand.remove('?R')
        hands = combs(hand, reds)

    elif '?B' in hand:
        hand.remove('?B')
        hands = combs(hand, blax)
    else:
        return [the_hand]
    return hands


def combs(fixed, opts):
    hands = []
    """ Retorna uma lista com todas as mãos possíveis trocando o coringa
    * fixed é a mão que não muda
    * opts é a lista de opções para o coringa
    
    * Tive que incluir os if not pra evitar que o coringa se tornasse uma carta
    igual a outra que ja existe na mao.
    """
    for cards in opts:
        aux = fixed[:]
        if type(cards) == list:
            if not(cards[0] in fixed):
                aux.append(cards[0])
            if not(cards[1] in fixed):
                aux.append(cards[1])
        if type(cards) == str:
            if not(cards in fixed):
                aux.append(cards)
        hands.append(aux)

    return hands

# ---------------------------------------------------------------------------#
# SOLUÇÃO NORVIG
# ---------------------------------------------------------------------------#

# Não entendi como a solução dele filtra, se filtra, as mãos com duas cartas
# iguais (afinal cada coringa pode virar qualquer carda de metade do baralho).

allranks = '23456789TJQKA'
redcards = [r+s for r in allranks for s in 'DH']
blackcards = [r+s for r in allranks for s in 'SC']


def best_wild_hand_norvig(hand):
    """Try all values for jokers in all 5-card selections."""
    hands = set(best_hand_norvig(h)
                for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)


def replacements(card):
    """Return a list of the possible replacements for a card.
    There will be more than 1 only for wild cards."""
    if card == '?B': return blackcards
    elif card == '?R': return redcards
    else: return [card]


# Essa função vem do hw_1_1
def best_hand_norvig(hand):
    return max(itertools.combinations(hand, 5), key=hand_rank)

# ---------------------------------------------------------------------------#

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'


# ------------------
# Provided Functions
#
# You may want to use some of the functions which
# you have already defined in the unit to write
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def straight(ranks):
    """Return True if the ordered
    ranks form a 5-card straight."""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def kind(n, ranks):
    """Return the first rank that this hand has
    exactly n-of-a-kind of. Return None if there
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None


def two_pair(ranks):
    """If there are two pair here, return the two
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

# hand_a = ['6C', '7C', '8C', '9C', 'TC', '5C', '?B']
# hand_b = ['TD', 'TC', '5H', '5C', '7C', '?R', '?B']
# nibla = "JD TC TH 7C 7D 7S 7H".split()
