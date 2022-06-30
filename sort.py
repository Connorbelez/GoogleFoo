# Please Pass the Coded Messages
# ==============================
#
# You need to pass a message to the bunny workers, but to avoid detection,
# the code you agreed to use is... obscure, to say the least. The bunnies
# are given food on standard-issue plates that are stamped with the numbers
# 0-9 for easier sorting, and you need to combine sets of plates to create the
# numbers in the code. The signal that a number is part of the code is that it
# is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger
# numbers like 144 and 414 are a little trickier. Write a program to help yourself
# quickly create large numbers for use in the code, given a limited number of plates
# to work with.
#
# You have L, a list containing some digits (0 to 9). Write a function solution(L)
# which finds the largest number that can be made from some or all of these digits
# and is divisible by 3. If it is not possible to make such a number, return 0 as
# the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear
# multiple times in the list, but each element in the list may only be used once.

l = [3, 1, 4, 1, 5, 9]

# testList =

l = [3,4,9,1,1]
def solution(l):
    import itertools
    num = sum(l)
    # check if no work needs be done
    if num % 3 == 0:
        listS = sorted(l, reverse=True)
        numStr = [str(nums) for nums in listS]
        num = "".join(numStr)
        num = int(num)
        return num
    l.sort(reverse=True)
    # Genate bitstrings of length len(l)-1
    for digits in range(len(l) - 1, 0, -1):
        testList = []
        # generate a list of indexes for 1s in a bitstring of length len(l)
        # of len(l) indexes, choose digits many indexes for 1s
        for bits in itertools.combinations(range(len(l)), digits):
            # initialize bitstring
            bitstring = ['0'] * len(l)

            # set each of the chosen indexes to 1
            for bit in bits:
                bitstring[bit] = '1'
            # bit string is now build
            # build the subset
            for j in range(len(bitstring)):
                if (bitstring[j] == "1"):  # if the bit at index j is 1 include element j in the subset.
                    testList.append(l[j])
            # test if this subset meets requirements.
            if (sum(testList) % 3 == 0):
                numStr = [str(nums) for nums in testList]
                num = "".join(numStr)
                num = int(num)
                return num
            testList = []
    return 0

print(solution(l))