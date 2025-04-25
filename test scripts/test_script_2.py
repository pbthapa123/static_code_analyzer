
# Function to add two numbers
def add_numbers(a, b):
    result = a + b   # Adds the inputs (can raise TypeError if types are incompatible)
    return result  #return the result of addition. 

def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"    # Handles division by zero gracefully
    return a / b                                # Returns the result of division


# Main function where execution starts
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
        print(f"Error: {e}")       # Catches and prints the error gracefully


# Entry point of the program
if __name__ == "__main__":
    main()