def add_numbers(a, b):
    sum = a + b
    return Sum  # Error: 'Sum' should be 'sum'

def divide_numbers(a, b):
    return a / b

def main():
    x = 10
    y = 0  # Error: division by zero will occur here
    result = divide_numbers(x, y)
    print("The result is:", result)
    
    a = 5
    b = "10"  # Error: invalid addition of int and string
    print(add_numbers(a, b))

if __name__ == "__main__":
    main()
