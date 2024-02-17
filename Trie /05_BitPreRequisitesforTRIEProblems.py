# Bits Pre-Requisites for the tries
1. Binary

Decimal = 9 and Binary 1001 (last 4 digits from right of binary) 
but in trie we always consider the entire bits sets 
Computer stores : 32 bits (int)  or 64 bits (long long)
0   0  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  0 0 0 0 0 0 0 0 0
31 30  29  28  27  26  25  24  23  22  21  20  19  18  17  16  15  14  13  12  11  10  9  8 7 6 5 4 3 2 1 0 
Note : This is read from from Right to Left and if you wan to find the greated number then left most bits has to be set i.e 1 in binary
since we have 1*2**0 = 1  
              1*2**3 = 8
        Sum          = 9
When the number will be having the largest value ?
When set bit present in the left most i.e 31, 30....etc..then number would be maximum

2. XOR
  
  XOR property
  1. Similary bits
     1 ^ 1 = 0
     0 ^ 0 = 0
  2. Different bits
     1 ^ 0 = 1
     0 ^ 1 = 0
  3. Even number of one's in binary will give you zero
     1 1 1 1
     1 1 1 1 => 1 ^ 1 = 0 => 0 ^ 1 = 1 =>  1 ^ 1 = 0
  4. Odd number of one's in binary will give you one
     1 1 1
     1 1 1 => 1 ^ 1 = 0 => 0 ^ 1 = 1 

3. How to check if ith bit is set or not ? (Do right shift)
   if ((num >> ith) & 1): # ith bit is 1 and then 1 & 1 = 1
     return True (set bit)
   else: return False (not set bit)

4. How do you turn or toggle a particular bits ? (Do left shift)
   (num | (1 << ith)) # 1 set to ith place and then do or operation so it will only flip the ith bit
