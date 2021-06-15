import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']


# Minha solução
def deal(numhands, n=5):
    return [[random.choice(mydeck) for i in range(n)] for j in range(numhands)]


# Solução Norvig:
def deal_norvig(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    """Shuffle the deck and deal out numhands n-card hands"""
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
# A solução dele meio que simula o que acontece com um baralho de verdade:
# embaralha e depois distribui a cartas em sequência:


# Solução Tura:

def hand(cards_qty):
    return [random.choice(mydeck) for i in range(cards_qty)]

def deal_tura(numhands, n=5):
    return [hand(n) for j in range(numhands)]

