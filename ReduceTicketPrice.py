# Question 4
def reduceTicketPrice(price, k):
    stack = []
    for digit in price:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1
    result = ''.join(stack).lstrip('0')
    return result if result else '0'

print("Test Case 1 -->")
price = input()
k = int(input())
print(reduceTicketPrice(price, k))
