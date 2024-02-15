"""a) Write a code taking as input a matrix A of size m × n and a vector bof size m×1, where m and n are arbitrarily
 large numbers and m < n,constructing the augmented matrix and performing 1. REF, and 2. RREF"""

#
def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # You can modify this part to take input from the user or use a different method to populate the matrix
            element = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Create a matrix
    my_matrix = create_matrix(rows, cols)

    # Display the created matrix
    print("\nThe Created Matrix:")
    print_matrix(my_matrix)

if __name__ == "__main__":
    main()




def print_matrix(matrix):
    for row in matrix:
        print([round(elem, 1) for elem in row])

def gaussian_elimination(matrix):
    rows, column = len(matrix), len(matrix[0])

    for i in range(rows):
        # Make the diagonal element 1
        divisor = matrix[i][i]
        if divisor == 0:
            # Choose a different row to avoid division by 0
            matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
            divisor = matrix[i][i]

        for j in range(column):
            matrix[i][j] = matrix[i][j] / divisor

        # Eliminate non-zero elements below the diagonal
        for k in range(i + 1, rows):
            factor = matrix[k][i]
            for j in range(column):
                matrix[k][j] = matrix[k][j] - (factor * matrix[i][j])

def reduced_row_echelon_form(matrix):
    rows, column = len(matrix), len(matrix[0])

    for i in range(rows - 1, 0, -1):
        for k in range(i - 1, -1, -1):
            factor = matrix[k][i]
            for j in range(column):
                matrix[k][j] -= factor * matrix[i][j]

def construct_augmented_matrix(A, b):
    return [row_a + [elem_b] for row_a, elem_b in zip(A, b)]

def find_pivot_nonpivot_columns(matrix):
    pivot_columns = []
    nonpivot_columns = []
    for j in range(len(matrix[0])):
        column = [matrix[i][j] for i in range(len(matrix))]
        if column.count(0) == len(column) - 1 and 1 in column:
            pivot_columns.append(j)
        else:
            nonpivot_columns.append(j)
    return pivot_columns, nonpivot_columns

def find_particular_solution(matrix):
    pivot_columns, nonpivot_columns = find_pivot_nonpivot_columns(matrix)
    particular_solution = [0] * len(matrix[0])
    for i in range(len(pivot_columns)):
        particular_solution[pivot_columns[i]] = round(matrix[i][-1], 1)
    return particular_solution

def find_solutions_to_ax_equals_0(matrix):
    pivot_columns, nonpivot_columns = find_pivot_nonpivot_columns(matrix)
    solutions_to_ax_equals_0 = []
    for j in nonpivot_columns:
        solution = [0] * len(matrix[0])
        solution[j] = 1
        for i in range(len(pivot_columns)):
            solution[pivot_columns[i]] = round(-matrix[i][j], 1)
        solutions_to_ax_equals_0.append(solution)
    return solutions_to_ax_equals_0

# Example usage:
rows = 5  # replace with your desired value
column = 7  # replace with your desired value
A = [[1, 2, 3, 4, 5, 6, 7],
     [8, 9, 1, 11, 2, 3, 4],
     [4, 6, 7, 18, 9, 0, 1],
     [2, 23, 4, 27, 6, 7, 8],
     [29, 30, 0, 0, 3, 3, 5]]

b = [1, 2, 3, 4, 5]

# Construct augmented matrix
augmented_matrix = construct_augmented_matrix(A, b)

print("Original Augmented Matrix:")
print_matrix(augmented_matrix)

# Apply Gaussian Elimination for Row Echelon Form (REF)
gaussian_elimination(augmented_matrix)

print("\nRow Echelon Form (REF):")
print_matrix(augmented_matrix)

# Apply Reduced Row Echelon Form (RREF)
reduced_row_echelon_form(augmented_matrix)

print("\nReduced Row Echelon Form (RREF):")
print_matrix(augmented_matrix)

# Identify Pivot and Non-pivot columns
pivot_columns, nonpivot_columns = find_pivot_nonpivot_columns(augmented_matrix)
print("\nPivot Columns:", pivot_columns)
print("Non-pivot Columns:", nonpivot_columns)

# Particular Solution
particular_solution = find_particular_solution(augmented_matrix)
print("\nParticular Solution:", particular_solution)

# Solutions to Ax = 0
solutions_to_ax_equals_0 = find_solutions_to_ax_equals_0(augmented_matrix)
print("\nSolutions to Ax = 0:")
for solution in solutions_to_ax_equals_0:
    print(solution)
