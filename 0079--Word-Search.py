class Solution:
    def dfs(self,row: int,col: int,idx) -> bool:
        if idx == len(self.word):
            return True
        
        pos = (row,col)

        if (
            col < 0 
            or
            row < 0
            or
            col >= self.cols
            or
            row >= self.rows
            or
            self.word[idx] != self.board[row][col]
            or
            pos in self.positions
        ):
            return False

        self.positions.add(pos)
        
        res = False
        for move_r,move_c in (
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ):

            if self.dfs(row+move_r,col+move_c,idx+1):
                res = True
                break
        return res   




    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])

        self.word = word
        self.board = board

        self.positions = set()

        for r in range(self.rows):
            for c in range(self.cols):
                if self.dfs(r,c,0):
                    return True




        return False
