

# Minha versão para card_ranks
def card_ranks_old(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r, s in cards]
    mapp = [('A', 14), ('K', 13), ('Q', 12), ('J', 11), ('T', 10)]

    for (u, v) in mapp:
        if u in ranks:
            ranks[ranks.index(u)] = v

    ranks = [int(a) for a in ranks]
    ranks.sort(reverse=True)
    return ranks


# Resposta do Norvig:
def card_ranks_norvig_old(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks


# Minha modificação para abranger o caso ace-low straight (5, 4, 3, 2, A):
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    if 2 and 3 and 4 and 5 and 14 in ranks:
        ranks.remove(14)
        ranks.append(1)
        return ranks
    return ranks


# Modificação do Norvig:
def card_ranks_norvig(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = [['--23456789TJQKA'].index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks
