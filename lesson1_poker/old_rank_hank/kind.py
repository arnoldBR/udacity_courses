

# Minha solução
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    rank_set = set(ranks)
    repites = {ranks.count(i):i for i in rank_set}
    if n in repites:
        return repites[n]
    return None


# Solução Norvig
def kind_norvig(n,ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

# Acho que fiquei bitolado de usar estruturas de dados sem necess...