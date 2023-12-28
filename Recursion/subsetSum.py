# Link : https://practice.geeksforgeeks.org/problems/subset-sums2234/1
# For each subset sum it, and then store it in subset sum aaray
# Idea is to use Pick and Not Pick Technique

# Approach One
nums = [1,2,3]
res = []
def dfs(idx, path):
    res.append(path.copy())
    for i in range(idx, len(nums)):
        path.append(nums[i])
        dfs(i+1, path)
        path.pop()
dfs(0, [])
return res

# Approach Two
arr = [2,3]
n = len(arr)
subsetSumArr = []

def subsetSum(i, total):
  if i == n:
    subsetSumArr.append(total)
    return
  subsetSum(i+1, total + arr[i]) # Pick
  subsetSum(i+1, total + 0) # not Pick

subsetSum(0,0)
subsetSumArr.sort()
return subsetSumArr

# Approach Three
# To Find Total subset sum without creating an array

arr = [2,3]
n = len(arr)
sumTotal = 0

def subsetSum(i, total):
  if i == n:
    return total
    
  leftSum = subsetSum(i+1, total + arr[i]) # Pick
  rightSum = subsetSum(i+1, total + 0) # not Pick
  return leftSum + rightSum

return subsetSum(0,0)


 
