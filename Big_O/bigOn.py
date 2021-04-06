import time

# O(n) - Linear Time
# As array grows bigger, time to complete function increases linearly. Count how many times the 
# function loops to complete. 8 values, 8 loops. O(8)
array = ['kobe', 'bruce', 'tim', 'jordan', 'nemo', 'alice', 'jas', 'ziggy']


def find_nemo(array):
    t0 = time.perf_counter()
    for index, name in enumerate(array):
        if name == 'nemo':
            print(f'Found Nemo at index: {index}')
    t1 = time.perf_counter()
    print(f'Time to search whole array: {t1-t0}')


find_nemo(array)
