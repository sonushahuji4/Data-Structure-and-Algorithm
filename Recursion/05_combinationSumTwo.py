
# Approach One

nums = [1,1,1,2,2]
n = len(nums)
target = 4
ans = []

def uniqeCombinationSum(ind, target, arr, n):
    if ind == n:
        if target == 0:
            ans.append(arr.copy())
        return
    if nums[ind] <= target:
        uniqeCombinationSum(ind+1, target - nums[ind], arr + [nums[ind]], n)
    uniqeCombinationSum(ind + 1, target, arr, n)

uniqeCombinationSum(0,target,[],n)
print(set(ans))
    
        
        

# Approach Two

ans = []
n = len(candidates)
  
def combinationSum(index, target, arr):
  if target == 0:
    ans.append(arr.copy())
    return

  for i in range(index, n):
    if i > index and candidates[i] == candidates[i-1]:
      continue
    if candidates[i] <= target:
      arr.append(candidates[i])
      combinationSum(i+1, target - candidates[i], arr)
      arr.pop()

combinationSum(0,target, [])
return ans

  
