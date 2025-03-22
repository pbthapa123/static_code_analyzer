import time

# Inefficient memory usage (list comprehension inside a loop)
x = [i for i in range(100)]

# Blocking operation
time.sleep(5)