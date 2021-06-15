# Minhas soluções:
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    for u in range(4):
        a = 1 - ranks[u] + ranks[u+1]
        if a != 0:
            return False
    return True


def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [v for u,v in hand]
    return suits[0] == suits[1] == suits[2] == suits[3] == suits[4]

# Soluções Norvig:
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # o que ele faz é verificar que diferença maxima é 4 e,
    # fazendo um set e verificando o tamanho desse set,
    # ele verifica se todas as cartas são diferentes.
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

