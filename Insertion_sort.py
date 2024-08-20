def insertion_sort(a):
    for i in range(len(a) - 1):  # range: i < len(a) - 1 or i <= len(a) - 2
        # i loop runs from zero to (n-2)

        for j in range(i + 1, 0, -1):
            if a[j] < a[j - 1]:
                swap(a, j, j - 1)
            else:
                break

def swap(a, first, second):  # first = j and second = j - 1
    temp = a[first]
    a[first] = a[second]
    a[second] = temp

# Test the insertion sort
a = [5, 4, 3, 6, 2, 1]
insertion_sort(a)
print(a)