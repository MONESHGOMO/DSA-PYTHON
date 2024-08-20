def selection_sort(a):
    for i in range(len(a)):
        end = len(a) - i - 1
        max_index = get_max(a, 0, end)
        swap(a, max_index, end)

def swap(a, max_index, end):
    temp = a[max_index]
    a[max_index] = a[end]
    a[end] = temp

def get_max(a, start, end):
    max_index = start
    for i in range(start, end + 1):
        if a[i] > a[max_index]:
            max_index = i
    return max_index

# Test the selection sort
a = [5, 3, 7, 4, 8, 2, 1]
selection_sort(a)
print(a)