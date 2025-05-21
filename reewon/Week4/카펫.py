import math

def solution(brown, yellow):
    answer = []
    # 가로: width, 세로: height
    width = int(0.5*((0.5*brown+2) + math.sqrt((brown*0.5+2)**2 - 4*(brown+yellow))))
    height = int(brown*0.5 - (width-2))
    if width < height:
        width = int(0.5*((0.5*brown+2) - math.sqrt((brown*0.5+2)**2 - 4*(brown+yellow))))
        height = int(brown*0.5 - (width-2))
    answer.append(width)
    answer.append(height)
    return answer
