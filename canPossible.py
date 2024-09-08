#Question 2
def canPossible(n, s, dictionary):
    
    for word in s.split():
      if word not in dictionary:
        return 0
    return 1
   
print("Test case 1 -->")
n = 6
s = "i like"
dictionary = ["i", "like", "sam", "sung", "samsung", "mobile"]
print(canPossible(n, s, dictionary))

print("__________")
print("Test case 2 -->")
n = 6
s = "i like samsung"
dictionary = ["i", "like", "sam", "sung", "samsung", "mobile"]
print(canPossible(n, s, dictionary))
