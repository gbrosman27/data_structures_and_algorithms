# Example for calculating Big O
# Assume input length = 5

def example_challenge(input):
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    while i < len(input): # O(n) Runs 5 times
        some_other_function() # O(n) Runs 5 times
        running = True # O(n) Runs 5 times
        a += 1 # O(n) Runs 5 times
    
    return a # O(1)

# Big O = O(3 + 4n) = O(n)

