

def solution(l):
    import itertools
    num = sum(l)
    if num%3==0:
        listS = sorted(l, reverse=True)
        numStr = [str(nums) for nums in listS]
        num = "".join(numStr)
        num = int(num)
        return num


    numPermutations = 2 ** len(l) #number of permutations of a bitstring = num subsets
    l.sort(reverse=True)
    print(l)
    testList = []
    for i in range(numPermutations, 0, -1):
        binary = bin(i)
        bitstring = list(binary)[2:]
        if len(bitstring) > len(l):
            # bin(1024 we will consider as a bitstring of just 0s
            continue
        if len(bitstring) < len(l):
            l1 = len(bitstring)
            l2 = len(l)
            for j in range(l2 - l1):
                bitstring.insert(0, 0)
                # if the length of the bitstring is less than the list, insert a zero at the beginning.
        print(bitstring)

        for j in range(len(bitstring)):
            if(bitstring[j] == "1"): #if the bit at index j is 1 include element j in the subset.
                print(l[j])
                testList.append(l[j])
        if(sum(testList) % 3==0):
            numStr = [str(nums) for nums in testList]
            num = "".join(numStr)
            num = int(num)
            return num
        testList = []
    return 0
