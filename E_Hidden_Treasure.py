n, clues = map(int,input().split())
left = 1
right = n
for _ in range(clues):

    clue = input().split()
    direction = clue[2]
    value = int(clue[4])
    if direction == 'left':
        right = value - 1
    else:
        left = value+1
    if right < left:
        print(-1)
        exit()
if right >= left:
        print(right-left+1)
        exit()

