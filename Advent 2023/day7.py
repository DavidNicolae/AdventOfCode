from collections import Counter

mpa = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 12, 'Q': 13, 'K': 14, 'A': 15}

def custom_sort_a(hand):
    return sorted(list(Counter(hand).values()), reverse=True), tuple(mpa[x] for x in hand)

def a():
    score = 0
    hands = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            cards, bid = line.split()
            hands.append((cards, int(bid)))
            line = f.readline()
    hands.sort(key=lambda h: custom_sort_a(h[0]))
    for idx, (_, bid) in enumerate(hands):
        score += (idx + 1) * bid

    return score

mpb = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 13, 'K': 14, 'A': 15}

def custom_sort_b(hand):
    c = Counter(hand)
    if 'J' in c:
        jokers = c.pop('J')
        if c:
            highest = max(c, key=c.get)
            c[highest] += jokers
        else:
            c['J'] = jokers
    
    return sorted(list(c.values()), reverse=True), tuple(mpb[x] for x in hand)

def b():
    score = 0
    hands = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            cards, bid = line.split()
            hands.append((cards, int(bid)))
            line = f.readline()
    hands.sort(key=lambda h: custom_sort_b(h[0]))
    for idx, (_, bid) in enumerate(hands):
        score += (idx + 1) * bid

    return score

if __name__ == '__main__':
    print(a())
    print(b())