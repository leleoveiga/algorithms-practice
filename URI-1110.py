while True:
    qt = int(input())
    if qt == 0: break

    cards = list(range(1, qt+1))
    discarded = []

    while len(cards) >= 2:
        cards.append(cards[1])
        cards.reverse()
        discarded.append(cards.pop())
        cards.pop()
        cards.reverse()

    dstr = "Discarded cards: "
    for i in range(len(discarded)):
        dstr += str(discarded[i])
        if i < len(discarded) - 1:
            dstr += ", "
    print(dstr)
    print(f"Remaining card: {cards[0]}")


