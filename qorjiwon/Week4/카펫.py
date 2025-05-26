def solution(brown, yellow):
    all = brown + yellow
    n = []
    for i in range(1, int(all**0.5) + 1):
        if all % i == 0:
            n.append((i, all // i))
    answer = []
    for w, h in n:
        if (w - 2) * (h - 2) == yellow:
            answer = [h, w]
            break
    return answer
