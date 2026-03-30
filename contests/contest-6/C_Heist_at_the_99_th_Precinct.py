tests = int(input())
for _ in range(tests):
    size = int(input())
    array = list(map(int,input().split()))
    counter = {}
    for el in array:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    found = False
    for c in counter.keys():
        if counter[c]%2 == 1:
            print('YES')
            found = True
            break
    if not found:
        print('NO')
        