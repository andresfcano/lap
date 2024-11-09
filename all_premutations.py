import numpy as np
import sys
import time

def generate_permutations(array):
    """
    Generate all permutations of the given array.
    """
    def permute(arr, start, end, result):
        if start == end:
            result.append(arr[:])
        else:
            for i in range(start, end + 1):
                arr[start], arr[i] = arr[i], arr[start]  # Swap
                permute(arr, start + 1, end, result)
                arr[start], arr[i] = arr[i], arr[start]  # Swap back

    result = []
    permute(array, 0, len(array) - 1, result)
    return result

def compute_total_cost(cost_matrix, assignment):
    """
    Compute the total cost of a given assignment.
    """
    total_cost = sum(cost_matrix[i, assignment[i]] for i in range(len(assignment)))
    return total_cost

def get_all_assignments(cost_matrix):
    """
    Get all possible assignments and their corresponding costs.
    """
    n = len(cost_matrix)
    indices = list(range(n))
    all_permutations = generate_permutations(indices)
    
    assignments = []
    costs = []
    max_cost = 0

    for perm in all_permutations:
        assignments.append(perm)
        costs.append(compute_total_cost(cost_matrix, perm))
        cost = compute_total_cost(cost_matrix, perm)
        if cost > max_cost:
            max_cost = cost
    
    return assignments, costs, max_cost

# Example usage
if __name__ == "__main__":
    cost_matrix = np.loadtxt(*sys.argv[1:])   
    
    # Start the timer
    start_time = time.time()
    
    assignments, costs, max_cost = get_all_assignments(cost_matrix)
    
    # Stop the timer
    end_time = time.time()
    
    # Calculate the duration
    duration = end_time - start_time
    
    print(f'Max cost: {max_cost}')
    print(f"Time taken: {duration:.4f} seconds")
