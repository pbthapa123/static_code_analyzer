# test_case_blocking_io_and_loop.py
import time

def read_file_slow():
    with open("example.txt", "r") as f:
        time.sleep(2)  # Simulate blocking I/O
        content = f.read()
    return content

def build_list_badly():
    numbers = []
    for i in range(1000):
        numbers = numbers + [i]  # Inefficient list construction
    return numbers
