# bubble sort

a = [5, 4, 8, 3, 0, 9, 2, 1]

for i in range(0, len(a)):
    for j in range(1, len(a) - i):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]

print(a)

'''
🪩 time complexity  = best case O(n) and worst case O(n^2)
🪩 space complexity  = O(1)
🪩 kunal kushwaha  
'''