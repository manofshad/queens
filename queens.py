from collections import defaultdict

ROWS = 8
COLS = 8

def validCoordinate(r, c):
    return (0 <= r < ROWS and 0 <= c < COLS)

def queenAttack(r, c):
    
    res = set()

    if not validCoordinate(r, c):
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
    queensAttackSquares = defaultdict(int) # (r, c) = count
    queens = set()

    def dfs(r, c):
        if len(queens) == 8:
            return queens
        
        if not validCoordinate(r, c):
            return None

        while True:
            if r >= 8:
                return
            
            if c < 7:
                nextRow = r
                nextCol = c + 1
            else:
                nextRow = r + 1
                nextCol = 0

            if validCoordinate(r, c) and queensAttackSquares[(r, c)] == 0:
                break
            else:
                r = nextRow
                c = nextCol

        attacks = queenAttack(r, c)
        for rAttack, cAttack in attacks:
            queensAttackSquares[(rAttack, cAttack)] += 1
        queens.add((r, c))
        val = dfs(nextRow, nextCol)
        
        if val:
            return val

        for rAttack, cAttack in attacks:
            queensAttackSquares[(rAttack, cAttack)] -= 1
        queens.remove((r, c))

        return dfs(nextRow, nextCol)

    return dfs(0, 0)

queen = [(0,0), (1, 0)]
        

print("starting eight_queens: ")
print(eight_queens())
