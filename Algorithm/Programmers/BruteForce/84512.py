def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    weirdDictionary = []
    count = 0
    
    for length in range(1, 6):
        if length == 1:
            weirdDictionary.extend(alphabets)
        else:
            newWord = []
            for prevWord in weirdDictionary[-5**(length-1):]:
                for alphabet in alphabets:
                    newWord.append(prevWord + alphabet)
            weirdDictionary.extend(newWord)
    
    weirdDictionary.sort()
    
    return weirdDictionary.index(word) + 1
    