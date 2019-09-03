
#       0,1,2,3 n=len(data) => 4


def reverseRecursion(data):
    start_pos = 0
    end_pos = 4
    i = -1
    if start_pos == end_pos:
        return
    else:
        i = i + 1
        print(data[i])
        return reverseRecursion(data[i])

data = [8,2,5,6]
