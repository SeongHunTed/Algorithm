def solution(citations):
    hIndices = []
    
    for citation in citations:
        h = citation
        larger = 0
        smaller = 0
        
        for item in citations:
            if item >= h:
                larger += 1
            
            if item < h:
                smaller += 1
                
        hIndices.append(min(citation, larger))

    return max(hIndices)
                