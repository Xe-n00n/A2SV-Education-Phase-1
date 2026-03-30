tests = int(input())
for _ in range(tests):
    length = int(input())
    decorations = map(int,input().split())
    decorations = sorted(decorations)
    min_distance = float('inf')

    for i in range(1,len(decorations)-1):
        distance = decorations[i+1]-decorations[i-1]
        if distance < min_distance:
            min_distance = distance
    
    print(min_distance)
    # maximum_count = 0
    # maximum_decoration = 0
    # counter = {}
    # for decoration in decorations:
    #     if decoration in counter.keys():
    #         counter[decoration] += 1
    #         if counter[decoration] == 3:
    #             # we already have 3 equal numbers
    #             print(0)
    #             exit()  
            
    #     else:
    #         counter[decoration] = 1
    #     if counter[decoration] > maximum_count:
    #         maximum_count = counter[decoration]
    #         maximum_decoration = decoration
    # desired_differece = 3 - maximum_decoration

    # for deco in sorted(decoration.keys()):
        

    