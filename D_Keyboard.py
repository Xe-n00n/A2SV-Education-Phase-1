tests = int(input())
for _ in range(tests):
    chars = list(input())
    res = set()
    i = 0
    while i < len(chars):
        j = i
        while j < len(chars) and chars[i] == chars[j]:
            j+=1 
        block_length = j - i
        
        if block_length%2 != 0:
            res.add(chars[i])
        i = j
    print(''.join(sorted(list(res))))