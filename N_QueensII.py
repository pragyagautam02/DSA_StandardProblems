class Solution:
    def totalNQueens(self, n: int) -> int:
            
        def solve(row,cols,diag,antidiag):
            if row==n:
                return 1
            
            ans=0
            for col in range(n):
                curr_col=col
                curr_diag=row-col
                curr_antidiag=row+col
                
                if curr_col in cols or curr_diag in diag or curr_antidiag in antidiag:
                    continue
                
                cols.add(curr_col)
                diag.add(curr_diag)
                antidiag.add(curr_antidiag)
                
                ans+=solve(row+1,cols,diag,antidiag)
                
                cols.remove(curr_col)
                diag.remove(curr_diag)
                antidiag.remove(curr_antidiag)
                
            return ans
    
        ans=solve(0,set(),set(),set())
        return ans
        
