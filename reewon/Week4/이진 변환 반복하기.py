def solution(s):
    zero_cnt = 0
    cnt = 0
    while s != "1":
        temp = [i for i in list(s) if i not in ['0']]
        zero_cnt += len(s) - len(temp)
        s = str(bin(len(temp))[2:])
        cnt += 1
    answer = [cnt, zero_cnt]
    return answer
