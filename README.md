# Assignment-3
Tutedude

Task 1: Calculate Factorial Using a Function

This Python program calculates the factorial of a given number using a function and displays the result.
Factorial of a number n is:
n!=n×(n−1)×(n−2)×...×1

Example:
5! = 5 × 4 × 3 × 2 × 1 = 120

This program calculates the factorial of a number using a user-defined function. First, a function named factorial() is created, which takes a single argument n. Inside the function, a variable result is initialized with the value 1, because factorial calculation is based on multiplication and starting with 1 prevents incorrect results. A for loop then runs from 1 to n, and in each iteration, the current value of i is multiplied with result, gradually building the factorial value. After the loop finishes, the function returns the final computed factorial. Outside the function, the program asks the user to enter a number, converts this input into an integer, and stores it in the variable num. Finally, the program prints the result by calling factorial(num) inside an f-string, which displays the factorial of the number entered by the user.



Task 2: Using the Math Module for Calculations

This program uses Python’s built-in math module to perform three mathematical operations on a number entered by the user: square root, natural logarithm, and sine value. First, the program imports the math module because functions like sqrt(), log(), and sin() are available only inside it. The user is then prompted to enter a number, which is converted into an integer and stored in the variable num. After that, the square root of the given number is calculated using math.sqrt(num) and stored in the variable square_root; the result is printed on the screen. Next, the program calculates the natural logarithm of the same number using math.log(num) and prints it. Finally, the program computes the sine value of the number (in radians) using math.sin(num) and displays the result. Thus, the code demonstrates how to import a module and apply different mathematical functions to user input.
