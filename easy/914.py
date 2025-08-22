def solution(deck):
    cards = {}
    for i in range(len(deck)):
        if deck[i] in cards:
            cards[deck[i]] += 1
        else:
            cards[deck[i]] = 1
    
    for i in range(2, min(set(cards.values())) + 1):
        divides = True
        for value in cards.values():
            if value % i != 0:
                divides = False
        if divides:
            return True
    return False
        
print(solution([1, 2, 3]))