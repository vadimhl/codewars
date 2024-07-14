# https://www.codewars.com/kata/524c74f855025e2495000262/train/python
def hand(hole_cards, community_cards):
    def rank(excl):
        return [ r for r,s in ranks.items() if s and r not in excl][:5]

    def nrank(n, excl = []):
        for r, s in ranks.items():
            if len(s) >= n and r not in excl:
                return r


    cards = hole_cards + community_cards
    # ♣ ♦ ♥ ♠
    rv = {'A':14, 'K':13, 'Q':12, 'J':11, '10':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2 }
    suits = {'♠':[], '♥':[], '♦':[], '♣':[] }
    ranks = {'A':[], 'K':[], 'Q':[], 'J':[], '10':[], '9':[], '8':[], '7':[], '6':[], '5':[], '4':[], '3':[], '2':[] }
    for card in cards:
        s, r = card[-1], card[:-1]
        suits[s].append(r)
        ranks[r].append(s)

    suits = {s[0] : sorted(s[1], key = lambda r:rv[r], reverse = True) for s in suits.items()}
    suits_diff = {}
    for s, r in suits.items():
        suits_diff[s] = [rv[r[i]]-rv[r[i+1]] for i in range(len(r)-1)]
    print(f'{suits=}')
    print(f'{suits_diff=}')
    print(f'{ranks=}')

    # 1 straight-flush
    for s, d in suits_diff.items():
        print(f'{s=} {d=}')
        if len(d) >= 4:
            print(f'{len(d)=}')
            for i in range(len(d)-3):
                if d[i:i + 4] == [1] * 4:
                    return ("straight-flush", suits[s][i: i + 5])

    # 2 four-of-a-kind
    r = nrank(4)
    if r:
        return ("four-of-a-kind", [r] + [rank([r])[0]])

    # 3 full house
    r3 = nrank(3)
    r2 = nrank(2, [r3])
    if r2 and r3:
        return ("full house", [r3, r2])
    
    # 4 flush
    for s, r in suits.items():
        if len(r) >= 5:
            return ("flush", r[:5])
        
    # 5 Straight
    rank_vals = [rv[r] for r, s in ranks.items() if s]
    straight = ''.join([chr(ord('0') + rank_vals[i]-rank_vals[i+1]) for i in range(len(rank_vals)-1)]).find('1111')
    if straight >= 0:
        return ('straight', [x for x in ranks if rv[x] in rank_vals[straight:]][:5])
    
    # 6 three-of-a-kind
    r3 = nrank(3)
    if r3:
        return ("three-of-a-kind", [r3]+rank(r3)[:2])

    # 7 two pair
    r2 = nrank(2)
    r2_2 = nrank(2, [r2])
    if r2 and r2_2:
        return ("two pair", [r2, r2_2, rank([r2, r2_2])[0]])

    # 8 pair
    if r2:
        return ("pair", [r2]+rank(r2)[:3])

    return ("nothing", rank([]))


hole_cards, community_cards = ["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]
hole_cards, community_cards = ["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]
hole_cards, community_cards = ["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"] # "straight-flush"
hole_cards, community_cards = ["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]
#hole_cards, community_cards = ["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"] # "full house"
hole_cards, community_cards = ["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"] # "flush"
hole_cards, community_cards = ["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"] # straight
hole_cards, community_cards = ["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]  # three-of-a-kind
hole_cards, community_cards = ["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"] # two pair
hole_cards, community_cards = ["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"] # pair
hole_cards, community_cards = ['J♣', 'A♥'], ['K♦', '3♥', 'J♥', 'J♠', 'J♦']
print(hand(hole_cards, community_cards))

# ['♦', '♠', '♣', '♥']