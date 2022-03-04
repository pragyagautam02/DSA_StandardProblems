class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def arrange(board):
            new_board=[]
            for row in board:
                new_board.append("".join(row))
                
            return new_board
                
            
        def solve(row,cols,diag,antidiag,board):
            if row==n:
                ans.append(arrange(board))
                return
            
            for col in range(n):
                curr_col=col
                curr_diag=row-col
                curr_antidiag=row+col
                
                if curr_col in cols or curr_diag in diag or curr_antidiag in antidiag:
                    continue
                
                cols.add(curr_col)
                diag.add(curr_diag)
                antidiag.add(curr_antidiag)
                board[row][col]="Q"
                
                solve(row+1,cols,diag,antidiag,board)
                
                board[row][col]="."
                cols.remove(curr_col)
                diag.remove(curr_diag)
                antidiag.remove(curr_antidiag)
                
        
        ans=[]
        initial=[["."]*n for i in range(n)]
        solve(0,set(),set(),set(),initial)
        return ans
        
