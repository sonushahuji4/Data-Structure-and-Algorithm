# Given an array of number arr and a number X,find the max value of arr[i] ^ X
# Note: Understand this problem how to solve then you'll be able to solve any problem which is related to XOR and tries

# Techniques to follow
# 1. Insert all the numbers in tri from the given array, but insert all the numbers in binary bits or format.
# 2. Take X and find max number from arry (beause tri contains all the integers in terms of binary) where number ^ x gives you maximum

# arr = [9,8,7,5,4] and X = 8
# Note : To have maximum value we need to have all the bits set to 1 i.e  11111, but is this possible, lets check
# Binary :  
[  9     8      7      5      4    ] and  X = 8
 01001 01000  00111  00101  00100           01000

check bit by bit from left to right
X =            0 1 0 0 0
Find arr[i]    0 0 1 1 1
---------------------------
Max Value      0 1 1 1 1   <= Max Value arr[i] ^ x




class TrieNode:
  def __init__(self):
    children = [None]*2 # Since binary numbers are 1 or 0
