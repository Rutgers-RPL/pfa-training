import numpy as np 

l1 = [[0.31, 0.43, 0.66],
      [0.81, 0.49, 0.52],
      [0.04, 0.39, 0.35]]

l2 = [[0.39, 0.23, 0.93],
      [0.40, 0.83, 0.76],
      [0.57, 0.46, 0.18]]

# METHOD 1: Loops

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Matrix Dimensions
rows_l1 = len(l1)
cols_l1 = len(l1[0])
cols_l2 = len(l2[0])

# Iterate through rows of l1
for i in range(rows_l1):
    # Iterate through columns of l2
    for j in range(cols_l2):
        # Iterate through rows of l2
        for k in range(cols_l1):
            result[i][j] += l1[i][k] * l2[k][j]

print(f'Method 1 (Loops): ') # Print method information
# Print the result matrix
for row in result:
    print(row)

# Method 2: List Comrehensions

# Matrix dimensions
rows_l1 = len(l1)
cols_l1 = len(l1[0])
cols_l2 = len(l2[0])

# Perform matrix multiplication using list comprehensions
result = [[sum(l1[i][k] * l2[k][j] for k in range(cols_l1)) for j in range(cols_l2)] for i in range(rows_l1)]

print(f'Method 2 (List Comprehension):') # Print method information
# Print the result matrix
for row in result:
    print(row)

# Method 3: NumPy
arr1 = np.array(l1)
arr2 = np.array(l2)
print(f'Method  (NumPy):') # Print method information
print(arr1@arr2)