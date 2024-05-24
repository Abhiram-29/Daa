import sys
from typing import List

def matrix_chain_order(p: List[int], n: int) -> tuple[List[List[int]], List[List[int]]]:
    """
    Compute the minimum number of scalar multiplications needed to compute the matrix
    chain product A[i]A[i+1]...A[j] and the optimal order of multiplication.

    Args:
        p (List[int]): List of dimensions of the matrices.
        n (int): Number of matrices.

    Returns:
        Tuple[List[List[int]], List[List[int]]]: m and s matrices, where m[i][j] stores the minimum
        number of scalar multiplications needed to compute the matrix chain product A[i]A[i+1]...A[j],
        and s[i][j] stores the index of the optimal split point in the subproblem.
    """
    m = [[0 for x in range(n)] for y in range(n)]
    s = [[0 for x in range(n)] for y in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_order(s: List[List[int]], i: int, j: int) -> None:
    """
    Print the optimal order of matrix multiplication for A[i]A[i+1]...A[j].

    Args:
        s (List[List[int]]): The s matrix computed by matrix_chain_order function.
        i (int): Start index of the matrix chain.
        j (int): End index of the matrix chain.
    """
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_order(s, i, s[i][j])
        print_optimal_order(s, s[i][j] + 1, j)
        print(")", end="")

n = int(input("Enter the number of matrices: ")) + 1

# Input the dimensions of matrices
matrix_dims = list(map(int, input("Enter the dimensions of matrices separated by spaces: ").split()))

# Get the order and the minimum number of multiplications
m, s = matrix_chain_order(matrix_dims, n)

print("Minimum number of multiplications is", m[1][n - 1])
print("Optimal order of multiplication is: ", end="")
print_optimal_order(s, 1, n - 1)
print()