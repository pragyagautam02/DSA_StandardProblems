class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_box_number(row,col):
            return ((row//3)*3 + col//3)
        
        def save_number(digit,row,col):
            rows[row][digit]+=1
            cols[col][digit]+=1
            boxes[find_box_number(row,col)][digit]+=1
            
        def can_be_placed(d,row,col):
            if (d not in rows[row]) and (d not in cols[col]) and (d not in boxes[find_box_number(row,col)]):
                return True
    
            return False
    
        def place_next_number(row,col):
            if row==N-1 and col==N-1:
                nonlocal solved_suduko
                solved_suduko = True
                
            elif col==N-1:
                backTrack(row+1,0)
            
            else:
                backTrack(row,col+1)
                
        def backTrack(row,col):
            if board[row][col]==".":
                for d in range(1,10):
                    if can_be_placed(d,row,col):
                        save_number(d,row,col)
                        board[row][col]=str(d)
                        place_next_number(row,col)
                        
                        if (not solved_suduko):
                            board[row][col]="."
                            del rows[row][d]
                            del cols[col][d]
                            del boxes[find_box_number(row,col)][d]
            
            else:
                place_next_number(row,col)

        
        N=9
        solved_suduko=False
        rows=[defaultdict(int) for i in range(N)]
        cols=[defaultdict(int) for i in range(N)]
        boxes=[defaultdict(int) for i in range(N)]
        
        for i in range(N):
            for j in range(N):
                if board[i][j]!=".":
                    digit=int(board[i][j])
                    save_number(digit,i,j)
                
        backTrack(0,0)
        
