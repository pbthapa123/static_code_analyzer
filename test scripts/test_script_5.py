
# test_case_blocking_io_and_loop.py
import time

def read_file_slow():
    with open("example.txt", "r") as f:
        time.sleep(2)            # Simulate blocking I/O: causes delay, not ideal in asynchronous or responsive programs
        content = f.read()       # Reads the entire content of the file after the delay
    return content               # Returns the content of the file after a simulated delay



def build_list_badly():
    numbers = []
    for i in range(1000):
        numbers = numbers + [i]  # Inefficient list construction: creates a new list each time, leading to poor performance
    return numbers               # Returns a list built inefficiently (using += in a loop is better)

