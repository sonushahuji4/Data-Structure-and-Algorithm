# Link : https://leetcode.com/problems/combination-sum/description/

# Approach One
ans = []
n = len(candidates)
def combinationSum(i,target,arr):
    if i == n:
        if target == 0:
            ans.append(arr.copy())
        return
    
    if candidates[i] <= target:
        arr.append(candidates[i])
        combinationSum(i,target - candidates[i], arr)
        arr.pop()
    combinationSum(i+1, target, arr)
  
combinationSum(0,target,[])
return ans

# Approach Two
ans = []
n = len(candidates)
def combinationSum(index, target, arr):
    if target == 0:
        ans.append(arr.copy())
        return
        
    for i in range(index, n):
        if candidates[i] <= target:
            arr.append(candidates[i])
            combinationSum(i, target - candidates[i], arr)
            arr.pop()
combinationSum(0, target, [])
return ans
      
      
      
  

