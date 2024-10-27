# https://leetcode.com/problems/accounts-merge/description/

from collections import defaultdict
from typing import List

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        nodeU = self.find(u)
        nodeV = self.find(v)

        if nodeU == nodeV:
            return 

        if self.size[nodeU] < self.size[nodeV]:
            self.parent[nodeU] = nodeV
            self.size[nodeV] += self.size[nodeU]
        else:
            self.parent[nodeV] = nodeU
            self.size[nodeU] += self.size[nodeV]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountsLength = len(accounts)
        dsu = DisjointSet(accountsLength)
        emailGroups = {}

        for i in range(accountsLength):
            for email in accounts[i][1:]:
                if email not in emailGroups:
                    emailGroups[email] = i
                else:
                    dsu.unionBySize(i, emailGroups[email])
        
        # Group emails by their representative
        components = defaultdict(list)
        for email, group in emailGroups.items():
            rootGroup = dsu.find(group)
            components[rootGroup].append(email)
        
        # Prepare the merged accounts
        mergedAccounts = []
        for group, emails in components.items():
            name = accounts[group][0]
            mergedAccount = [name] + sorted(emails)
            mergedAccounts.append(mergedAccount)

        return mergedAccounts
