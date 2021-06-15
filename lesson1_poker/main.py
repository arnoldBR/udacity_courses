from allmax import allmax
from hand_rank import hand_rank


def poker(hands):
    """Returns the best hand: poker([hand,...])=> hand

    Utilização: no console, importar:
    from deal import deal
    from main import poker

    - distribuir as mãos com a função deal.
    - aplicar poker para obter a mão vencedora.

    """
    # Minha solução - não sei se funciona
    return max(hand_rank(hand) for hand in hands)


# Solução Norvig:
def poker_norvig(hands):
    return allmax(hands, key=hand_rank)