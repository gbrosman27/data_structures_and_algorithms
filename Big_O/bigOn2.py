# O(n^2) - Quadratic Time
# As number of elements increase, number of operations increase quadratically. ex. (2 elements, 3 operations), (3 elements, 9 operations), (4 elements, 81 operations)
# Becomes slow very quickly as elements increase. Avoid this!


# Log all pairs of an array
boxes = ["a", "b", "c", "d", "e"]

def log_all_pairs(array):
    for i in array: # O(n)
        for j in array: # O(n) (Nested loop)
            print(i, j) # O(n)

log_all_pairs(boxes)

# When loops are nested, multiply them.
# O(n * n) = O(n^2) = Quadratic Time