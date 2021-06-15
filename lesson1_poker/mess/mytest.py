def card_ranks(cards):
    """Return a list of the ranks, sorted with higher first."""
    ranks = [r for r, s in cards]

    mapp = [('A', 14), ('K', 13), ('Q', 12), ('J', 11), ('T', 10)]

    for (u, v) in mapp:
        if u in ranks:
            ranks[ranks.index(u)] = v

    ranks.sort(reverse=True)
    return ranks

card_ranks(['AC', '3D', '4S', 'KH'])

