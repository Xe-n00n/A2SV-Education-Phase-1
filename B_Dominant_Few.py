"""
1 2 3 6 8 


2 3 4 5

"""


tests = int(input())
for _ in range(tests):
    n = int(input())
    players = map(int, input().split())
    players = sorted(players)
    i = 2
    j = n - 2
    leftSum = players[0] + players[1]
    rightSum = players[n-1]
    possible = False
    while i <= j :
        if leftSum < rightSum:
            possible = True
            break
        
        rightSum += players[j]
        leftSum += players[i]
        i += 1
        j -= 1
    if leftSum < rightSum:
        possible = True
    if possible:
        print('YES')
    else:
        print('NO')