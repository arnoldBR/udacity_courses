# allmax é criada para resolver o caso de empate que max() não resolve
from hand_rank import hand_rank


# Minha solução
def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    rmax = max(iterable, key=hand_rank)
    return [hand for hand in iterable if hand_rank(hand) == hand_rank(rmax)]

# solução do norvig:
def allmax_norvig(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

