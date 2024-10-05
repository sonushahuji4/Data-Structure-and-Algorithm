# Link : https://leetcode.com/problems/subsets/

# Approach One 1.0

nums = [3,1,2]
n = len(nums)
ans = []
def subsetAll(ind,arr,n):
    if ind == n:
        ans.append(arr.copy())
        return
    subsetAll(ind + 1, arr + [nums[ind]], n)
    subsetAll(ind + 1, arr, n)

subsetAll(0,[],n)
print(ans)


# Approach One 1.1

allSubset = []
def generateAllSubSet(nums,i,n,subset):
    if i >= n: 
        allSubset.append(subset.copy())
        return
    
    subset.append(nums[i]) # Pick
    generateAllSubSet(nums,i+1,n,subset)
    subset.pop() # Not Pick
    generateAllSubSet(nums,i+1,n,subset)
  
generateAllSubSet(nums,0,len(nums),[])
return allSubset

# Approach Two

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
