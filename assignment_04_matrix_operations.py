# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
# =============================================================================


def read_matrix(name="Matrix"):
    """Read an M x N matrix from the user using nested loops."""
    print(f"\n--- Enter {name} ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) != cols:
                print(f"  Error: expected {cols} values, got {len(row_input)}. Try again.")
                continue
            row = []
            for value in row_input:
                row.append(float(value) if "." in value else int(value))
            matrix.append(row)
            break

    return matrix, rows, cols


def display_matrix(matrix, title="Matrix"):
    """Display a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")
    if not matrix:
        print("  (empty)")
        return

    # Determine the widest element for alignment
    width = 0
    for row in matrix:
        for val in row:
            width = max(width, len(str(val)))

    for row in matrix:
        line = ""
        for val in row:
            line += str(val).rjust(width + 2)
        print(line)


# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
def transpose_matrix(matrix, rows, cols):
    """Return the transpose of an M x N matrix (N x M result)."""
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
def add_matrices(matrix_a, matrix_b, rows, cols):
    """Return the element-wise sum of two M x N matrices."""
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b, m, n, p):
    """Multiply an M x N matrix A by an N x P matrix B -> M x P result."""
    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):          # rows of A
        for j in range(p):      # columns of B
            total = 0
            for k in range(n):  # shared dimension
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


# =============================================================================
# MAIN PROGRAM
# =============================================================================
def main():
    print("=" * 50)
    print("MATRIX OPERATIONS PROGRAM")
    print("=" * 50)

    while True:
        print("\nChoose an operation:")
        print("  A - Transpose a Matrix")
        print("  B - Add Two Matrices")
        print("  C - Multiply Two Matrices")
        print("  Q - Quit")
        choice = input("Enter choice: ").strip().upper()

        if choice == "A":
            matrix, rows, cols = read_matrix("Matrix")
            display_matrix(matrix, "Original Matrix")
            transposed = transpose_matrix(matrix, rows, cols)
            display_matrix(transposed, "Transposed Matrix")

        elif choice == "B":
            matrix_a, rows_a, cols_a = read_matrix("Matrix A")
            print(f"\nMatrix B must be the same size as Matrix A ({rows_a} x {cols_a}).")
            matrix_b, rows_b, cols_b = read_matrix("Matrix B")

            if rows_a != rows_b or cols_a != cols_b:
                print("Error: Matrices must be the same size to add them.")
                continue

            display_matrix(matrix_a, "Matrix A")
            display_matrix(matrix_b, "Matrix B")
            result = add_matrices(matrix_a, matrix_b, rows_a, cols_a)
            display_matrix(result, "Sum (A + B)")

        elif choice == "C":
            matrix_a, rows_a, cols_a = read_matrix("Matrix A (M x N)")
            print(f"\nMatrix B must have {cols_a} rows (to match Matrix A's columns).")
            matrix_b, rows_b, cols_b = read_matrix("Matrix B (N x P)")

            if cols_a != rows_b:
                print("Error: Columns of A must equal rows of B for multiplication.")
                continue

            display_matrix(matrix_a, "Matrix A")
            display_matrix(matrix_b, "Matrix B")
            result = multiply_matrices(matrix_a, matrix_b, rows_a, cols_a, cols_b)
            display_matrix(result, "Product (A x B)")

        elif choice == "Q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter A, B, C, or Q.")


if __name__ == "__main__":
    main()
