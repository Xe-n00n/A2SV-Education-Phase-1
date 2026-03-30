n = int(input())
sereja = 0
dima = 0
cards = list(map(int,input().split()))
i = 0
j = n-1
serejaTurn = True
while i <= j:
    if cards[i] > cards[j]:
        if serejaTurn:
            sereja += cards[i]
        else:
            dima += cards[i]
        i += 1        
    else:
        if serejaTurn:
            sereja += cards[j]
        else:
            dima += cards[j]
        cards.pop(j)
        j -= 1
    serejaTurn = not serejaTurn



print(f'{sereja} {dima}')
