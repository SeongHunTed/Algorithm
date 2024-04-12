def strToInt(time):
    hour = int(time[0:2]) * 60 * 60
    minute = int(time[3:5]) * 60
    sec = int(time[6:])
    
    return hour + minute + sec
    
def intToStr(time):
    hour = time // 3600
    minute = (time % 3600) // 60
    sec = (time % 3600) % 60
    
    strTime = str(hour).zfill(2) + ":"
    strTime += str(minute).zfill(2) + ":"
    strTime += str(sec).zfill(2)
    return strTime
    
def solution(play_time, adv_time, logs):
    playTime = strToInt(play_time)
    adTime = strToInt(adv_time)
    dp = [0] * (playTime + 1)
    
    for log in logs:
        start = strToInt(log.split("-")[0])
        end = strToInt(log.split("-")[1])
        dp[start] += 1
        dp[end] -= 1
        
    # 현재 보고 있는 사람들의 합 
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i-1]
    
    # 사람들이 시청할 수 있는 누적합
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i-1]
        
    maxCount = dp[adTime]
    answer = 0
    
    for i in range(1, playTime):
        end = i + adTime
        if i + adTime >= playTime:
            end = playTime
        
        if maxCount < dp[end] - dp[i]:
            maxCount = dp[end] - dp[i]
            answer = i + 1
    
    return intToStr(answer)