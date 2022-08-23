class NQueens:
    '''
    def backtrack_nqueen(row = 0, count = 0):
        for col in range(n):
            # iterate through columns at the curent row.
            if is_not_under_attack(row, col):
                # explore this partial candidate solution, and mark the attacking zone
                place_queen(row, col)
                if row + 1 == n:
                    # we reach the bottom, i.e. we find a solution!
                    count += 1
                else:
                    # we move on to the next row
                    count = backtrack_nqueen(row + 1, count)
                # backtrack, i.e. remove the queen and remove the attacking zone.
                remove_queen(row, col)
        return count
    '''
    def totalNQueens(self, n: int) -> int:
        diag1 = set()
        diag2 = set()
        usedCols = set()

        return self.helper(n, diag1, diag2, usedCols, 0)
 
 
    def helper(self, n, diag1, diag2, usedCols, row):
        '''
        NOTES: 
        1. Top level scans through all cols in row 0
        sub processes takes care of the rest of rows
        2. The use of 
            row + col for anti-diagonal
            row - col for diagonal
        '''
        solutions = 0
        if row == n:
            return 1
 
        for col in range(n):
            if row + col in diag1 or row - col in diag2 or col in usedCols:
                continue
            print('row:', row, 'col:', col)
            diag1.add(row + col)
            diag2.add(row - col)
            usedCols.add(col)
            print('add no go:', diag1, diag2, usedCols)
            solutions += self.helper(n, diag1, diag2, usedCols, row + 1)
            print('solution:', solutions)
            # backtrack no go conditions
            diag1.remove(row + col)
            diag2.remove(row - col)
            usedCols.remove(col)
            print('backtrack no go:', diag1, diag2, usedCols)

        return solutions