puppies = int(input())
colors = list(input())
if puppies == 1:
    print('Yes')
    exit()
colors_counter = [0]*26
for color in colors:
    colors_counter[ord(color)-ord('a')] += 1

possible = False
for count in colors_counter:
    if count >= 2:
        possible = True

if possible:
    print('Yes')
else:
    print('No')

"""
abababc

acacac
"""