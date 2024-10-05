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

  
