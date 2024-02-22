def solution(s):
    s = s.lower()
    strings = s.split(" ")
    
    processed = [word.capitalize() for word in strings]
    
    return ' '.join(processed)