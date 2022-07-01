s1 = "<<>><"
s2 = ">----<"

def solution(s):
    crossTally = 0
    rHeading = []
    lHeading = []

    sList = list(s)
    for i in range(len(sList)):
        if sList[i] == ">":
            rHeading.append(i)
        if sList[i] == "<":
            lHeading.append(i)

    for rIndex in rHeading:
        for lIndex in lHeading:
            if rIndex < lIndex:
                crossTally +=1
    return crossTally*2

print(solution(s1))
print(solution(s2))