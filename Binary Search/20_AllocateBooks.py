# https://www.naukri.com/code360/problems/allocate-books_1090540?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries

def findPages(arr: [int], n: int, m: int) -> int:

    def getAllcateBooks(pages, arr, n):
        studentCount = 1
        studentPages = 0
        for i in range(n):
            if studentPages + arr[i] <= pages:
                studentPages += arr[i]
            else:
                studentCount += 1
                studentPages = arr[i]
        return studentCount

    low = max(arr)
    high = sum(arr)

    if m > n: return -1

    while low <= high:
        mid = low + (high - low) // 2
        numberOfStudentsAllocated = getAllcateBooks(mid, arr, n)
        if numberOfStudentsAllocated > m:
            low = mid + 1
        else:
            high = mid - 1
    return low
