tests = int(input())
for _ in range(tests):
    n = int(input())
    array = []
    for _ in range(n):
        i,j = map(int,input().split())
        somme = i+j
        array.append([somme,i,j])
    
    array=sorted(array)
    result = []
    for somme, i, j in array:
        result.append(i)
        result.append(j)
    
    print(*result)