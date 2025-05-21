# Function checking addition
def add(a, b):
    return a + b

# Function checking subtraction
def subtract(a, b):
    return a - b

# Function checking subtraction
def multiply(a, b):
    return a * b

# Function checking division
def divide(a, b):
    if b == 0:
        return float("nan")
    return a / b

# Function checking concatenation
def concatenate(a, b):
    return f"{a}{b}"
