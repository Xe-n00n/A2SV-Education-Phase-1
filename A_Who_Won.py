tests = int(input())

for _ in range(tests):
    beforeX, beforeY = map(int,input().split())
    afterX, afterY = map(int,input().split())

    if (beforeX > beforeY and afterX < afterY) or (beforeX < beforeY and afterX > afterY):
        print('NO')
    else:
        print('YES')