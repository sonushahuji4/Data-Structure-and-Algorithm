# Link : https://practice.geeksforgeeks.org/problems/subset-sums2234/1
# For each subset sum it, and then store it in subset sum aaray
# Idea is to use Pick and Not Pick Technique

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

 
