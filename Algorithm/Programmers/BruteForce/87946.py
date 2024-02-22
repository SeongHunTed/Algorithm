import math
import itertools
def solution(k, dungeons):
    
    nPr = list(itertools.permutations(dungeons, len(dungeons)))
    maxVisit = 0
    
    for sequence in nPr:
        hp = k
        visit = 0
        for dungeon in sequence:
            demand, waste = dungeon[0], dungeon[1]
            if hp >= demand:
                hp -= waste
                visit += 1
        
        maxVisit = max(visit, maxVisit)
    
    return maxVisit