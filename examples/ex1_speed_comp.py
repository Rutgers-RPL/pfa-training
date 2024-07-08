import time
import numpy as np

def matrix_multiply_for_loop(l1, l2):
    t1 = time.time() # Record starting time
    
    # Determine the dimensions of matrices l1 and l2
    rows_l1 = len(l1)      # Number of rows in l1
    cols_l1 = len(l1[0])   # Number of columns in l1 (should equal number of rows in l2 for multiplication)
    cols_l2 = len(l2[0])   # Number of columns in l2
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_l2)] for _ in range(rows_l1)]
    
    # Perform matrix multiplication using nested loops
    for i in range(rows_l1):      # Iterate over rows of l1
        for j in range(cols_l2):  # Iterate over columns of l2
            for k in range(cols_l1):  # Iterate over columns of l1 (or rows of l2)
                # Multiply corresponding elements and accumulate the sum
                result[i][j] += l1[i][k] * l2[k][j]
    
    return time.time()-t1 # Return total compute time


def matrix_multiply_list_comprehension(l1, l2):
    t1 = time.time() # Record starting time
    
    # Determine the dimensions of matrices l1 and l2
    rows_l1 = len(l1)      # Number of rows in l1
    cols_l1 = len(l1[0])   # Number of columns in l1 (should equal number of rows in l2 for multiplication)
    cols_l2 = len(l2[0])   # Number of columns in l2
    
    # Perform matrix multiplication using list comprehensions
    result = [[sum(l1[i][k] * l2[k][j] for k in range(cols_l1)) for j in range(cols_l2)] for i in range(rows_l1)]
    
    return time.time()-t1 # Return total compute time

def matrix_multiply_np(arr1, arr2):
    t1 = time.time() # Record starting time
    arr3 = arr1@arr2
    return time.time()-t1 # Return total compute time

def main():
    for i in range(11):
        print(f'Test {i}: {2**i}^2')
        a1 = np.random.rand(2**i, 2**i)
        a2 = np.random.rand(2**i, 2**i)
        
        print(f'For Loop Solve Time: {matrix_multiply_for_loop(a1.tolist(), a2.tolist())}')
        print(f'List Comprehension Solve Time: {matrix_multiply_list_comprehension(a1.tolist(), a2.tolist())}')
        print(f'NumPy Solve Time: {matrix_multiply_np(a1, a2)}')
        print('---')

if __name__ == '__main__':
    main()
    


