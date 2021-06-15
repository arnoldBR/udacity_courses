# Esta função é só para reproduzir os percentuais de ocorrencia de cada mao
# no poker (wikipedia)


def hand_percentages(n=100):
    pass


def hand_percentages_norvig(n=700*1000):
    """Sample n random hands and print a table of percentages for each type
     of hand"""
    counts = [0] * 9
    for i in range(n//10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print("%14s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n))

hand_names = {
    0:"High Card",
    1:"Pair",
    2:"2 Pair",
    3:"3 Kind",
    4:"Straight",
    5:"Flush",
    6:"Full house",
    7:"4 Kind",
    8:"Straight Flush",
}

