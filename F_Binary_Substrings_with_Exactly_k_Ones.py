k = int(input())
s = list(input())
freq = {}
freq[0] = 1

ones_count = 0
result = 0

for c in s:
    if c == '1':
        ones_count += 1
    
    result += freq[ones_count - k]
    if ones_count in freq:
        freq[ones_count] += 1
    else:
        freq[ones_count] = 1
print(result)