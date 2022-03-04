class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def find_box_number(row,col):
            return ((row//3)*3 + col//3)
        
        def save_number(digit,row,col):
            rows[row][digit]+=1
            cols[col][digit]+=1
            boxes[find_box_number(row,col)][digit]+=1

        
        N=9
        rows=[defaultdict(int) for i in range(N)]
        cols=[defaultdict(int) for i in range(N)]
        boxes=[defaultdict(int) for i in range(N)]
        
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    digit=board[i][j]
                    save_number(digit,i,j)
                    
        for row in range(N):
            for col in range(N):
                if board[row][col] != ".":
                    digit=board[row][col]
                    if rows[row][digit]>1 or cols[col][digit]>1 or boxes[find_box_number(row,col)][digit]>1:
                        return False
        
        return True
