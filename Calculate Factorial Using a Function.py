# Function to calculate factorial of a number
# formula factorial of n = n * (n-1) * (n-2) * ... * 1


def factorial(n):  # Defining the function, which takes one argument n
    result = 1  # Initializing result variable to 1
    for i in range(1, n + 1):  # Looping from 1 to n (n+1 is excluded)
        result *= i  # Multiplying result by i in each iteration
    return result  # Returning the final result


# taking user input
num = int(input("Enter a number: "))

# printing result
print(f"Factorial of {num} is: {factorial(num)}")
