def solution(s):
    myDict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    
    answer = ""  # 문자열로 초기화
    key = ""
    for char in s:
        if char.isdigit():
            answer += char  # 바로 숫자를 문자열에 추가
        else:
            key += char  # 문자를 key에 추가
            if key in myDict:  # key가 myDict에 있으면
                answer += str(myDict[key])  # 해당 숫자를 문자열로 변환하여 answer에 추가
                key = ""  # key 초기화
    
    return int(answer)  # 최종적으로 문자열을 정수로 변환하여 반환
