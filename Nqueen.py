class NQueens:
    def _init_(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def is_safe(self, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        return True
# for i in range(row,-1,-1) and for j in range(col,-1,-1)


    def solve(self, row):
        if row >= self.n:
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve(row + 1):
                    return True
                # Backtrack
                self.board[row][col] = 0

        return False

    def print_solution(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()


def solve_n_queens(n):
    n_queens = NQueens(n)
    if n_queens.solve(0):
        n_queens.print_solution()
    else:
        print("No solution exists.")


# Example usage:
n = 4
solve_n_queens(n)