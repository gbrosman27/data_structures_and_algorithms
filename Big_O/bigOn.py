# O(n) - Linear Time
# As array grows bigger, time to complete function increases linearly. 
# Without break statement after finding nemo, 8 values, 8 loops. (9 values, 9 loops, so on...)

import time

array = ['kobe', 'bruce', 'tim', 'jordan', 'nemo', 'alice', 'jas', 'ziggy']


def find_nemo(array):
    t0 = time.perf_counter() # O(1)
    for index, name in enumerate(array): # O(n) Runs 8 times
        if name == 'nemo': # O(n) Runs 8 times
            print(f'Found Nemo at index: {index}') # O(1)
    t1 = time.perf_counter() # O(1)
    print(f'Time to search whole array: {t1-t0}') # O(1)


find_nemo(array)

# Rule 1 - Worst Case Scenario
# Best case, Nemo is at start of the array and we only have to loop one time.
# Worst case, Nemo is at end of the array and we have to loop the whole array (8 times).

# Rule 2 - Drop the Constants
# Above function gives us O(2n + 4).
# Drop the constants to simplify. Big O for above function becomes O(n).

# Rule 3 - Different Terms for Inputs
# If function has multiple parameters and multiple loops (not nested), calculate loops separately. O(a + b) shows two linear loops.
# If multiple loops are nested, multiply them. O(a * b).

# Rule 4 - Drop Non-Dominants
# A function may have a loop outside of 2 loops that are nested. This is written O(n + n^2). The quadratic part
# is the most significant as it will slow down the function quicker than the linear loop. So we can drop the O(n)
# and write this as O(n^2).


# Keep code readable and scalable (speed (time complexity), memory (space complexity)).
# Space complexity can be manipulated by variables, function calls, data structures, and allocations.