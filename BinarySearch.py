#binary search


'''
 time complexity= best case : O(log n) ,worst case O(n)
 space complexity = O(1)
https://www.javatpoint.com/binary-search-in-java

'''
a = [5, 6, 7, 8, 9, 10]
target = 8

start = 0
end = len(a) - 1

while start <= end:

    mid = start + (end - start) // 2
    if a[mid] == target:
        print(mid)
        break

    elif a[mid] < target:
        start = mid + 1
    elif a[mid] > target:
        end = mid - 1

    else:
        print("-1")

