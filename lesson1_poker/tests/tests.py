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