def is_solved(board):
    h_lines = [[board[y][x] for x in range(3)] for y in range(3)]
    v_lines = [[board[y][x] for y in range(3)] for x in range(3)]
    d_lines = [
        [board[i][i] for i in range(3)],
        [board[i][3-i-1] for i in range(3)]
    ]
    lines = h_lines + v_lines + d_lines

    is_board_full = True
    for line in lines:
        if len([x for x in line if x == 1]) == 3:
            return 1
        if len([x for x in line if x == 2]) == 3:
            return 2
        if len([x for x in line if x == 0]) > 0:
            is_board_full = False

    if is_board_full:
        return 0
    return -1
