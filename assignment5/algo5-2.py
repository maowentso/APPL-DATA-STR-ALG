
##Input: 1 2 3 4 5 6 7 8

##Output: 7

##Input: 1 1 1 1 1 1 1 1

##Output: 7

import sys
valid_solutions = []
current_sol = [0] * 8

def is_safe(row, col):
    for prev_col in range(col):
        prev_row = current_sol[prev_col]
        if prev_row == row or abs(prev_row - row) == abs(prev_col - col):
            return False
    return True

def generate_all_solutions(col=0):
    if col == 8:
        valid_solutions.append(list(current_sol))
        return
    
    for row in range(1, 9):
        if is_safe(row, col):
            current_sol[col] = row
            generate_all_solutions(col + 1)

generate_all_solutions()


def solve_min_moves(initial_board):
    min_moves = 8
    
    for sol in valid_solutions:
        current_moves = 0
        for col in range(8):
            if initial_board[col] != sol[col]:
                current_moves += 1
        if current_moves < min_moves:
            min_moves = current_moves
            
    return min_moves

while True:
    try:
        line = input()
        if not line.strip():
            continue
        initial_board = [int(x) for x in line.split()]
        result = solve_min_moves(initial_board)
        print(result)
                
    except (IOError, EOFError):
        break

