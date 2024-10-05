# Link : https://leetcode.com/problems/subsets-ii/description/

# Approach One

n = len(nums)
nums.sort()
subsetArr = []
def subsetSum(i, ans):
    if i == n:
        data = ans.copy()
        if data not in subsetArr:
            subsetArr.append(data)
        return
    ans.append(nums[i]) # Pick
    subsetSum(i+1,ans)
    ans.pop() # Not Pick
    subsetSum(i+1,ans)

subsetSum(0,[])
return subsetArr

# Approach Two

nums.sort()
unique_combinations = []
n = len(nums)

def solve(i, arr):
    unique_combinations.append(arr.copy())
    
    for ind in range(i,n):
        if ind > i and nums[ind] == nums[ind - 1]:
            continue

        arr.append(nums[ind])
        solve(ind + 1, arr)
        arr.pop()
        
solve(0, [])
return unique_combinations
