def solution(n, words):
    wordList = set()
    target = 0
    turn = 0
    lastword = ''
    
    for word in words:
        if target // n >= 1:
            target = 0
            turn += 1
            
        if lastword != '' and lastword[-1] != word[0]:
            return [target+1, turn+1]
        
        if word in wordList:
            return [target+1, turn+1]
        
        wordList.add(word)
        lastword = word
        target += 1
        
    return [0, 0]