'''
🪩 time complexity =O(n) ,O(n^2)
🪩space complexity = O(1)
'''
a = [1, 43, 8, 3, 68, 34, 67]
target = 68
index = 0
for i in range(0, len(a) - 1):
    if a[i] == target:
        index = i
        break
if index != 0:
    print("element found at index ", index)
else:
    print("element not found in the list ")
