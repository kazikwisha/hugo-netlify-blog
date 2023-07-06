#
def findNumber(arr, k):
    if int(k) in arr:
        print("YES")
    else:
        print("NO")


array = []
n = len(array)

for _ in range(int(n)):
    array.append(int(input()))

key = int(input().strip())
# get integer list split by ","
array = list(map(int, input().split(',')))
# driver code to test
# key = 8
# array = [5,8,9,3]
findNumber(array, key)

# Enter this in the input prompt dialog box
# http://code.sololearn.com/python

# 8
# 5,8,9,3

# Note:The first line we enter "key"
# Second line we enter the "array" without the "[ ]" brackets
