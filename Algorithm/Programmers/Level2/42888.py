from collections import deque

def parseToList(records):
    result = []
    user = dict()
    
    for record in records:
        messages = record.split()
        event = messages[0]
        uid = messages[1]
    
        if event == "Leave": continue

        user[uid] = messages[2]

    for record in records:
        messages = record.split()
        event = messages[0]
        uid = messages[1]
        
        if event == "Enter":
            result.append(user[uid] + "님이 들어왔습니다.")
        elif event == "Leave":
            result.append(user[uid] + "님이 나갔습니다.")
        
    return result

def solution(record):
    answer = parseToList(record)
    return answer