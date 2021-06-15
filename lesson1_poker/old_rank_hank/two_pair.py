from old_rank_hank.kind import kind


# Minha solução
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    if len(set(ranks)) == 3:
        pairs = []
        for u in ranks:
            if not (u in pairs) and ranks.count(u) == 2:
                pairs.append(u)
        return tuple(pairs)
    return None


# Solução do Norvig
def two_pair_norvig(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return pair, lowpair
    else:
        return None
