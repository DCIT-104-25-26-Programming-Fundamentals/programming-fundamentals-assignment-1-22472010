# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
def print_first_n_terms(n):
    """Print the first N terms of the Fibonacci sequence on one line."""
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
 
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
 
    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))
 
 
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
def is_fibonacci_number(num):
    """Return True if num is a Fibonacci number, using a loop (no recursion)."""
    if num < 0:
        return False
 
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
 
    return False
 
 
# =============================================================================
# MAIN PROGRAM
# =============================================================================
def main():
    print("=" * 50)
    print("FIBONACCI SEQUENCE GENERATOR")
    print("=" * 50)
 
    # --- Part A ---
    try:
        n = int(input("\nHow many terms? "))
    except ValueError:
        n = -1  # will trigger the error message below
 
    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_first_n_terms(n)
 
    # --- Part B ---
    try:
        num = int(input("\nEnter a number to check: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
 
    if is_fibonacci_number(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")
 
 
if __name__ == "__main__":
    main()
