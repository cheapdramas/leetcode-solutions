class Solution:
    def backtrack(self,row:int) -> None:
        if row == self.n:
            self.total += 1
            return 
        for col in range(self.n):
            pos_idx = row + col
            neg_idx = row - col

            if (
                col in self.cols
                or
                pos_idx in self.pos_diags
                or 
                neg_idx in self.neg_diags
            ):
                continue
            
            self.cols.add(col)
            self.pos_diags.add(pos_idx)
            self.neg_diags.add(neg_idx)

            self.backtrack(row + 1)

            self.cols.remove(col)
            self.pos_diags.remove(pos_idx)
            self.neg_diags.remove(neg_idx)



        


    
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.total = 0
        self.pos_diags = set()
        self.neg_diags = set()
        self.cols = set()


        self.backtrack(0)

        return self.total
