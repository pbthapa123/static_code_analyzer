
# test_case_memory_nested_loops.py

def allocate_memory():
    big_list = [x * 2 for x in range(10**6)]  # Large memory usage: creates a list with 1 million elements
    return big_list          # Returns a large list that consumes significant memory

def nested_loops():
    for i in range(1000):
        for j in range(1000):
            result = i * j  # Deep nested loop (inefficient in some cases)
