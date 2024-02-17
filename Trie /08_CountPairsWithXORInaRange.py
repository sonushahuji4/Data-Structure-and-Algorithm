# Link : https://leetcode.com/problems/count-pairs-with-xor-in-a-range/description/


from collections import defaultdict
from typing import List

class BinaryTrieNode:
    def __init__(self):
        self.children = defaultdict(BinaryTrieNode)
        self.count = 0
        
        
class BinaryTrie:
    def __init__(self, maxbits=None):
        self.root = BinaryTrieNode()
        self.maxbits = maxbits
        
    def insert(self, value):
        node = self.root
        for i in reversed(range(self.maxbits)):
            node_value = (value >> i) & 1
            node.children[node_value].count += 1
            node = node.children[node_value]
            
    def count_pairs_within_range(self, value, high):
        count_pairs = 0
        node = self.root
        for i in reversed(range(self.maxbits)):
            if not node:
                break
                
            high_at_bit_i = (high >> i) & 1
            value_at_bit_i = (value >> i) & 1
            if high_at_bit_i:
                if value_at_bit_i in node.children:
                    count_pairs += node.children[value_at_bit_i].count
                node = node.children.get(1 - value_at_bit_i, None)
            else:
                node = node.children.get(value_at_bit_i, None)
                
        return count_pairs
                

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        max_bits = len(bin(max(nums + [high+1]))) - 2
        
        ans = 0
        trie = BinaryTrie(max_bits)
        for num in nums:
            ans += trie.count_pairs_within_range(num, high+1) - trie.count_pairs_within_range(num, low)
            trie.insert(num)
                        
        return ans
