def queenAttack(r, c):
    ROWS = 8
    COLS = 8
    res = set()

    if not (0 <= r < ROWS or 0 <= c < COLS):
        print("Not Valid coordinate")
        return

    # Vertical
    for row in range(ROWS):
        res.add((row, c))

    # Horizontal
    for col in range(COLS):
        res.add((r, col))

    for i in range(8):
        if 0 <= r + i < ROWS and 0 <= c + i < COLS:
            res.add((r + i, c + i))
        if 0 <= r - i < ROWS and 0 <= c - i < COLS:
            res.add((r - i, c - i))
        if 0 <= r - i < ROWS and 0 <= c + i < COLS:
            res.add((r - i, c + i))
        if 0 <= r + i < ROWS and 0 <= c - i < COLS:
            res.add((r + i, c - i))

    return res


def validQueens(queens):
    board = [[False] * 8 for _ in range(8)]

    for r, c in queens:
        if board[r][c] == True:
            return False

        attacks = queenAttack(r, c)

        for rAttack, cAttack in attacks:
            board[rAttack][cAttack] = True
            
        # print(board)

    return True


def eight_queens():
    queens = set()

    def dfs(r, c):
        if not validQueens(queens):
            return None
        
        if len(queens) == 8:
            return queens.copy()
        
        if r >= 8:
            return
        
        if c < 7:
            nextRow = r
            nextCol = c + 1
        else:
            nextRow = r + 1
            nextCol = 0
            
        queens.add((r, c))
        val = dfs(nextRow, nextCol)
        
        if val:
            return val
        
        queens.remove((r, c))
        return dfs(nextRow, nextCol)

    return dfs(0, 0)

queen = [(0,0), (1, 0)]
        

print("starting eight_queens: ")
print(eight_queens())
