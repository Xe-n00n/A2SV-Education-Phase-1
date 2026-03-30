tests= int(input())
for _ in range(tests):
    n = int(input())
    array = list(map(int,input().split()))
    target = int(input())
    if target >= min(array) and target <= max(array):
        print('YES')
    else:
        print('NO')
