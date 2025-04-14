# test_case_memory_nested_loops.py

def allocate_memory():
    big_list = [x * 2 for x in range(10**6)]  # Large memory usage
    return big_list

def nested_loops():
    for i in range(1000):
        for j in range(1000):
            result = i * j  # Deep nested loop (inefficient in some cases)
