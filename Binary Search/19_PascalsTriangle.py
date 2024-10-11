# https://leetcode.com/problems/pascals-triangle/description/

1                   1
2                1      1
3              1    2     1
4          1     3     3     1 
5      1      4     6     4     1


There are 3 kinds of questions that will be asked
1. Given row R and column C, tell me the element at that place.
   Example R = 5, C = 3
   Answer is 6
2. Print any nth row of the pascals Triangle
   Example N = 5
   Answer 1 4 6 4 1
3. Given N, print entire pascal triangle
   Example N = 5
   Answer is 
   1                   1
   2                1      1
   3              1    2     1
   4          1     3     3     1 
   5      1      4     6     4     1

Let's solve 1st type of question

given R and C do
(R - 1)                 n
        C           =    C  =  n!/(r! * (n-r)!)
          (C - 1)         r

after some observaion
10
  C   = (10 * 9 * 8) / (1 * 2 * 3)
    3

def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def get_element(R, C):
    return nCr(R - 1, C - 1)

# Example:
R = 5
C = 3
print(get_element(R, C))  # Output: 6



Let's solve 2nd type of question

Appraoch One

def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def print_pascals_row(n):
    row = []
    for c in range(n):
        row.append(nCr(n - 1, c))
    return row

# Example usage:
N = 5
print(print_pascals_row(N))  # Output: [1, 4, 6, 4, 1]


Approach Two

ans = 1
formula is -> ans = (row - col)//col

def generate_pascals_row(n):
    row = [1]  # First element is always 1
    for i in range(1, n):
        # Each element is row[i-1] * (n-i) // i
        row.append(row[i - 1] * (n - i) // i)
    return row

# Example usage:
N = 5
print(generate_pascals_row(N))  # Output: [1, 4, 6, 4, 1]


Let's solve 3rd type of question

Approach One

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pascalTringle = []
        for i in range(numRows):
            row = [1]
            if pascalTringle:
                lastRow = pascalTringle[-1]
                for j in range(len(lastRow)-1):
                    row.append(lastRow[j] + lastRow[j+1])
                row.append(1)
            pascalTringle.append(row)
        return pascalTringle


Approach Two

def generate_pascals_triangle(n):
    triangle = []
    
    for i in range(n):
        # Start with the first element as 1
        row = [1]
        for j in range(1, i+1):
            # Each element is calculated based on the previous row's values
            row.append(row[j-1] * (i - j + 1) // j)
        triangle.append(row)
    
    return triangle

# Function to print the triangle nicely
def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

# Example usage:
N = 5
triangle = generate_pascals_triangle(N)
print_pascals_triangle(triangle)

