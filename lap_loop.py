import os
import numpy as np
import subprocess
import time

def resize_matrix(file_path, n):
    """
    Completely replace the matrix with random numbers of size n x n and save it back to the file.
    
    Parameters:
    - file_path (str): Path to the file containing the matrix.
    - n (int): Desired size for the n x n matrix.
    """
    random_matrix = np.random.randint(1, 10, size=(n, n))
    with open(file_path, 'w') as f:
        for row in random_matrix:
            f.write(' '.join(map(str, row)) + '\n')

def run_lap(mtx_file, gamma=1e-2):
    """
    Run the LAP script and measure execution time.
    
    Parameters:
    - mtx_file (str): Input file for the LAP script.
    - gamma (float): Regularization parameter for the Sinkhorn algorithm.
    
    Returns:
    - float: Time taken to execute the LAP script.
    """
    start_time = time.time()
    subprocess.run(['python', 'lap.py', mtx_file, str(gamma)], check=True)
    end_time = time.time()
    return end_time - start_time

def main():
    # File path for the input matrix
    mtx_file = "cost.dat"
    gamma = 1e-2
    iterations = 100
    sizes = [9, 10, 11, 12]
    
    # Store average times for each size
    results = {}

    for n in sizes:
        print(f"Running for n = {n}")
        total_time = 0

        for _ in range(iterations):
            # Step 1: Generate a new matrix
            resize_matrix(mtx_file, n)

            # Step 2: Run the LAP script and measure time
            time_taken = run_lap(mtx_file, gamma)
            total_time += time_taken

        # Calculate the average time
        avg_time = total_time / iterations
        results[n] = avg_time
        print(f"Average time for n = {n}: {avg_time:.4f} seconds")

    # Display results
    print("\nSummary of Results:")
    for n, avg_time in results.items():
        print(f"n = {n}: Average Time = {avg_time:.4f} seconds")

if __name__ == "__main__":
    main()
