# 34번 불통과 코드
def replacement(data):
    data = data.replace('C#', 'c')
    data = data.replace('D#', 'd')
    data = data.replace('F#', 'f')
    data = data.replace('G#', 'g')
    data = data.replace('A#', 'a')
    data = data.replace('B#', 'b')
    
    return data

def solution(m, musicinfos):
    answer = ''
    m = replacement(m)
    
    maxTime = 0
    for music in musicinfos:
        start, end, title, codes = music.split(",")
        codes = replacement(codes)
        
        runtime = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
        index = 0
        value = ''
        
        time = runtime
        
        while time:
            value += codes[index]
            if index + 1 == len(codes):
                index = -1
            index += 1
            time -= 1
            
        if m in value:
            if answer:
                if maxTime >= runtime:
                    continue
            maxTime = runtime
            answer = title
            
    if answer:
        return answer
    else:
        return "(None)"
    
# 28번 30번 불통과 코드
# def solution(m, musicinfos):
#     answer = ''
    
#     myDict = {}
#     titles = []
    
#     for info in musicinfos:
#         start, end, title, codeString = info.split(",")
#         startHour, startMinute = map(int, start.split(":"))
#         endHour, endMinute = map(int, end.split(":"))
#         if endHour == "00":
#             endHour = 24
#             endMinute = 0
#         runTime = endHour * 60 + endMinute - (startHour * 60 + startMinute)
#         titles.append(title)
        
#         codes = []
#         for i in range(len(codeString)):
#             if codeString[i] == "#":
#                 codes[-1] = codes[-1] + "#"
#             else:
#                 codes.append(codeString[i])
                
#         length = len(codes)
#         loop = runTime // length
#         left = runTime % length
        
#         play = loop * codes + codes[:left]
#         play = "".join(play)
        
#         if play in myDict:
#             myDict[play].append(title)
#         else:
#             myDict[play] = [title]
    
#     keys = list(myDict.keys())
    
#     mlist = []
#     for i in range(len(m)):
#         if m[i] == "#":
#             mlist[-1] = "#" + mlist[-1]
#         else:
#             mlist.append(m[i])
    
#     mString = " ".join(mlist)
    
#     candidates = {}
    
#     for key in keys:
#         klist = []
#         for i in range(len(key)):
#             if key[i] == "#":
#                 klist[-1] = "#" + klist[-1]
#             else:
#                 klist.append(key[i])
#         kString = " ".join(klist)
        
#         if mString in kString:
#             if len(key) in candidates:
#                 candidate[len(key)].append(key)
#             else:
#                 candidates[len(key)] = [key]
    
#     if len(list(candidates.keys())) == 0:
#         return "(None)"
    
#     maxKey = max(list(candidates.keys()))
#     targetKeys = candidates[maxKey]
    
#     answer = []
#     for key in targetKeys:
#         answer.append(myDict[key])
    
#     if len(answer) >= 2:
#         print("Hi")
#         minIndex = 999999
#         for item in answer:
#             minIndex = min(titles.index(item), minIndex)
#         answer = titles[minIndex]
    
#     return answer[0][0]