from collections import defaultdict


def valid_solution(board):
    lines_to_check = defaultdict(list)

    for row_idx, row in enumerate(board):
        for col_idx, val in enumerate(row):
            if val == 0:
                return False
            block_idx = row_idx // 3 * 3 + col_idx // 3

            lines_idx = [row_idx, col_idx+9, block_idx+18]
            for i in lines_idx:
                if val not in lines_to_check[i]:
                    lines_to_check[i].append(val)
                else:
                    return False
