def add_numbers(a, b):
    result = a + b
    return result

def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    x = 10
    y = 0  # Error: division by zero will occur here
    result = divide_numbers(x, y)
    print("The result is:", result)

    a = 5
    b = "10"  # Error: invalid addition of int and string
    try:
        print(add_numbers(a, b))  # This will raise a TypeError
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()