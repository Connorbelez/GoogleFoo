def solution(x, y):
    generations = 0
    x,y = int(x),int(y)
    while x > 1 or y > 1:
        if x > y:
            x = x-y
        elif x < y:
            y = y-x
        else:
            x = x-y
        generations +=1
        if x < 1 or y < 1:
            return "impossible"
    return str(generations)

solution("4","7")