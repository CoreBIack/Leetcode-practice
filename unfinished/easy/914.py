def solution(deck):
    cards = {}
    for i in range(len(deck)):
        if deck[i] in cards:
            cards[deck[i]] += 1
        else:
            cards[deck[i]] = 1

    if len(set(cards.values())) == 1 and set(cards.values()).pop() != 1:
        return True
    return False

print(solution([1, 2, 3]))