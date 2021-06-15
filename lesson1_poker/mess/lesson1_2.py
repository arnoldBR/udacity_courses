# Minha primeira solução
def ss(nums):
    n = 0

    for num in nums:
        n = n + num * num

    return n


# Outra maneira
def ss2(nums):
    sq = [x * x for x in nums]
    return sum(sq)


# Solução do Norvig:
def ss3(nums):
    return sum(x ** 2 for x in nums)


def poker(hands):
    """Returns the best hand: poker([hand,...])=> hand
    """
    # Minha solução - não sei se funciona
    # return max(hand_rank(hand) for hand in hands)
    # Solução Norvig:
    return max(hands, key=hand_rank)





# Função de teste
def test():
    """Test cases foe the functions in poker game."""
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".slipt()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == sf
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    return "tests pass"
