#Question 1
def findPairs(nums):
    hm = {}
    for num in nums:
        if num in hm:
            hm[num] += 1
        else:
            hm[num] = 1
    res = []
    for key in hm.keys():
        if hm[key] == 1:
            res.append(key)
    return res

test1 = [1,2,3,2,1,4]
print("Test Case 1 -->", findPairs(test1))

test2 = [2,1,3,2]
print("Test Case 2 -->", findPairs(test2))

