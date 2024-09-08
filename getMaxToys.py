def getMaxToys(price, money):
    left = 0
    currSum = 0
    maxToys = 0
    for right in range(len(price)):
        currSum += price[right]

        while currSum > money:
            currSum -= price[left]
            left += 1
        
        maxToys = max(maxToys, right - left + 1)
    return maxToys

print("Test Case 1 -- >")
price = [1,2,5,3,2,1,6]
money = 6
print(getMaxToys(price, money))