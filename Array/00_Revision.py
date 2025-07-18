1 Two Sum (Unsorted)

When given an unsorted array, and need to find two elements matching a target sum, use a hash map to store each number’s index while iterating. 
Check if target - current number exists in the map. This gives O(n) time and O(n) space.


2 Two Sum II (Sorted)

When given a sorted array, and need to find two elements matching a target sum, use the two-pointer approach: start with one pointer at the beginning and one at the end, 
move them inward depending on the sum. This avoids extra space and reduces time to O(n).

3 3Sum

When given an array and need to find triplets summing to zero (or any target), first sort the array, 
then fix one element at a time and use the two-pointer approach on the remaining subarray to find pairs that sum to -fixed element. 
Sort helps handle duplicates and enables efficient pair searching. 
Time complexity is O(n²).

4. Trapping Rain Water (Prefix & Suffix Max Approach)

Precompute a prefix max array (maximum height to the left of each position) and a suffix max array (maximum height to the right). 
At each index, trapped water = min(prefix_max[i], suffix_max[i]) - height[i]. 
This approach is intuitive and works in O(n) time and O(n) space.

5. 3Sum Closest

Sort the array first, then for each index, fix one element and use the two-pointer approach on the remaining subarray to find the pair that makes the sum closest to the target. 
Update the closest sum whenever a better one is found. 
Works in O(n²) time and helps avoid checking all triplets naively.

6. Next Permutation

To find the next lexicographical permutation, scan from right to left to find the first decreasing element (pivot). 
Then, find the smallest element on the right larger than the pivot, swap them, and finally reverse the subarray to the right of the pivot. 
This transforms the current sequence into the next greater permutation in-place in O(n) time.

7. Rotate Image

To rotate an n × n matrix by 90° clockwise in-place, first transpose the matrix (convert rows to columns), then reverse each row. 
This effectively moves elements layer by layer without extra space. 
Works in O(n²) time and constant space.


8. Container With Most Water

Use the two-pointer approach: start with pointers at both ends, compute area as width × min(height[left], height[right]), and move the pointer with the shorter line inward to potentially find a taller line and increase area. 
Repeat until pointers meet. 
Runs in O(n) time and uses constant space.

9. Spiral Matrix

Use four boundary pointers (top, bottom, left, right) to simulate peeling layers in spiral order. 
Traverse right, down, left, and up while shrinking the boundaries inward each time. 
Repeat until all elements are visited. Works in O(m × n) time and constant extra space.

10. Group Anagrams

Use a hash map (dictionary) where the key is a sorted version of each string (or a character count tuple), and the value is a list of anagrams sharing that key. 
This groups all anagrams together efficiently in O(n * k log k) time, where k is the max string length.

11. Group Anagrams (without sorting)

Use a hash map where the key is a 26-length tuple of character counts (one slot per lowercase letter). 
For each string, build its count tuple and use it to group anagrams. 
This avoids sorting and runs in O(n * k), where n = number of strings and k = max string length.

  
12. Sort the Matrix Diagonally

Use a hash map to collect each diagonal’s elements, using i - j as the key since all cells on the same diagonal share this difference. 
Sort each diagonal list, then write back into the matrix in-place. 
Runs in O(m * n log k), where k is the diagonal length.


13. Diagonal Traverse

Iterate diagonals grouped by the same i + j index sum. 
For each diagonal, reverse the order when moving upwards (even diagonals) and keep as is when moving downwards (odd diagonals). 
Collect elements into a result list while traversing each group. Runs in O(m × n).

                                                                           
14. Sort Colors

Use the Dutch National Flag (three-pointer) approach: maintain three pointers — low, mid, and high. 
Traverse the array with mid, swap 0s to the front (low) and 2s to the back (high), leaving 1s in the middle. 
Solves in one pass, O(n) time, and constant space.


15. Find Original Array From Doubled Array

Sort the array first. Use a counter (hash map) to track frequencies. 
Iterate from smallest to largest: for each element x, if count of 2×x is less than count of x, return empty. 
Otherwise, decrement counts and add x to original array. 
Works in O(n log n) time due to sorting.

  
16. Sum of Even Numbers After Queries

Keep a running sum of even numbers. For each query, if the original value at index is even, subtract it from sum first. 
Then update the value. If the new value is even, add it back to sum. 
This avoids recomputing the entire even sum repeatedly and achieves O(1) per query, O(n + q) overall.

  
17. Find Pivot Index

Approach One (Prefix & Suffix):
Build prefix and suffix sum arrays. For each index, if prefix sum equals suffix sum, that index is the pivot. 
Easy to visualize but uses O(n) extra space. Time: O(n), Space: O(n).

Approach Two (Optimized Running Sums):
Use a running left sum and compute right sum on the fly as total sum - left sum - nums[i]. 
Check at each index if left sum equals right sum. 
Saves space and runs in one pass. Time: O(n), Space: O(1).


18. Increasing Triplet Subsequence

Greedily track two smallest increasing numbers (first, second). 
If you find a number bigger than second, you have a triplet → return True. 
Runs in O(n) time and O(1) space.

  
19. Largest Perimeter Triangle

Sort sides descending. Check triplets from largest: if largest side < sum of other two, valid triangle → return their sum as max perimeter. 
Else, continue. O(n log n) time from sorting.


20. Contains Duplicate II

Use a hash map (dictionary) to store the last index of each number as you iterate.
For each element, check if it already exists in the map and if the index difference is ≤ k.
If so, return True immediately.
Otherwise, update the index in the map.
This approach runs in O(n) time and uses O(n) space.


21. Set Mismatch

Use a counting array or hash set to detect which number appears twice (duplicate), and which is missing (no occurrence).
Alternatively, use math: expected sum and actual sum difference gives missing - duplicate.
Time: O(n)
Space: O(1) if modifying input (e.g., marking negative), otherwise O(n).
Example: For [1, 2, 2, 4], duplicate is 2, missing is 3.

                                
22. Continuous Subarray Sum

Use a prefix sum with modulo k to check if the same remainder has appeared before (at least two elements apart).
If two prefix sums have the same mod value, the subarray sum in between is divisible by k.
Use a hash map to store first occurrence of each mod.
Time: O(n)
Space: O(min(n, k))
Example: For [23, 2, 4, 6, 7], k = 6 → mod repeats with remainder 0 → subarray sum divisible by 6.


23. Shortest Path in a Grid with Obstacles Elimination

Use BFS to explore all possible paths from (0, 0) to (m-1, n-1), while tracking the remaining obstacles you can eliminate (k).
For each cell, store (row, col, remaining_k) as state in a visited set to avoid revisiting with the same or fewer eliminations left.
At each step, decrement k if you step onto an obstacle.
Stop and return steps when you reach the target.
Time: O(m * n * k) since each cell can be visited with different remaining k values.
Space: O(m * n * k).

Example:
For grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1 → you can eliminate at most one obstacle and reach the end in 6 steps.


24. Toeplitz Matrix Check

Check if all elements in each top-left to bottom-right diagonal are the same.
Use a hash map (or dictionary) with key = (row - col) to group and compare diagonal elements.
If any element does not match the first value in its diagonal, return False.
Time: O(m * n), Space: O(m + n) for storing diagonals.
Example:
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]] → All diagonals have identical elements → return True.


25. Ball Simulation in Grid

Simulate each ball's path row by row:

* If cell is 1, ball moves right; if cell is -1, ball moves left.
* Check for "V" shape blockers:

  * At 1, if next cell is -1 or at right wall → stuck.
  * At -1, if prev cell is 1 or at left wall → stuck.
* Track final column or mark -1 if stuck.

Time: O(m \* n), simulate each ball individually.
Space: O(n) for output.

Example:
grid = \[\[1,1,1,-1,-1],\[1,1,1,-1,-1],\[-1,-1,-1,1,1],\[1,1,1,1,-1],\[-1,-1,-1,-1,-1]]
→ Output: \[1, -1, -1, -1, -1].

26. Valid Sudoku

Check Row, Column, and Box Uniqueness
Use three data structures to track digits:
One for each row.
One for each column.
One for each 3×3 sub-box (index: (r // 3) * 3 + (c // 3)).

Approach:
Iterate each cell.
Ignore empty cells (".").
Check if the current digit is already in the row, column, or box → return False if so.
Otherwise, add digit to row, column, and box.
Two options for implementation:
Set-based (simple and clear).
Bitmask-based (optimized for space & faster checks).
Time: O(1) since board size is fixed (9×9).
Space: O(1).

27. Prefix Sum & Reverse Sum Tracking
Approach 1: Prefix + Suffix sums (explicit suffix tracking)
Build a prefix sum array.
For each index i, calculate:
Prefix sum up to i ⇒ average of first i + 1 elements.
Suffix sum from i + 1 onward ⇒ average of remaining elements (or 0 if none).
Track the index with the smallest absolute difference between these two averages.
Time: O(n)
Space: O(n) (for prefix array)

Approach 2: Prefix sum + total sum (optimized space)
Compute total sum first.
As you iterate left to right, maintain running prefix sum.
At each index i:
Left average = prefix sum // (i + 1).
Right average = (total sum - prefix sum) // (n - i - 1), or 0 if no elements remain.
Update min difference and track the index.
Time: O(n)
Space: O(1)

28. 2389. Longest Subsequence With Limited Sum 
(Greedy + Prefix Sum + Binary Search)
To find the longest subsequence with sum ≤ each query:
Sort nums to pick smallest elements first (maximize count under budget).
Build a prefix sum array, where prefix[i] = sum of first i+1 smallest elements.
For each query, use binary search to find how many elements fit (i.e., largest i where prefix[i] ≤ query).
This avoids checking all combinations and leverages sorted greediness.
🕒 Time:
O(n log n + m log n) → n = nums.length, m = queries.length
Sorting + prefix + binary search per query
🧠 Space: O(n) for prefix array and O(m) for output
📌 Example:
nums = [4, 5, 2, 1], queries = [3, 10, 21]
→ Sorted: [1, 2, 4, 5], prefix: [1, 3, 7, 12]
→ Output: [2, 3, 4] (2 elements ≤ 3, 3 elements ≤ 10, all 4 ≤ 21)
