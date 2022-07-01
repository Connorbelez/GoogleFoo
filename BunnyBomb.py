
def solution(x,y):
    generations = 0
    x,y = int(x),int(y)
    while x > 1 or y > 1:

        if x > y:
            print("X:",x,"Y:",y)


            truncatedQ = x // y
            if(x%y) == 0:
                truncatedQ = truncatedQ-1

            print("Truncated: ",truncatedQ)

            x = x-y*truncatedQ

            # print("X AFTER:",x,"Y after:",y)
            generations += truncatedQ
            if truncatedQ == 0:
                return "impossible"
        elif x < y:
            # print("X:",x,"Y:",y)
            truncatedQ = y // x
            if(y%x) == 0:
                truncatedQ = truncatedQ-1
            # print("Truncated: ",truncatedQ)
            y = y-x*truncatedQ
            # print("X AFTER:",x,"Y after:",y)
            generations += truncatedQ

            if truncatedQ == 0:
                return "impossible"
        else:
            return "impossible"
        if x < 1 or y < 1:
            print(x,y)
            return "impossible"
    return str(generations)

print(solution("4","8"))
