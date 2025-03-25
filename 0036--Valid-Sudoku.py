class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #check if each row have unique values
        subboards = [
            [],
            [],
            []
        ]
        coords = []
        
        for row_index in range(len(board)):
            if row_index % 3 == 0:
                for subboard in subboards:
                    if len(subboard) != len(set(subboard)):
                        return False
                subboards = [
                    [],
                    [],
                    []
                ]
            row = board[row_index]
            #row without dots
            clear_row = []
            for index,element in enumerate(row):
                if element != ".":
                    
                    #subboards appending
                    if index <= 2:
                        if element not in subboards[0]:
                            subboards[0].append(element)
                        else:
                            return False

                    if index > 2 and index <= 5:
                        if element not in subboards[1]:
                            subboards[1].append(element)
                        else:
                            return False
                    if index > 5 and index <= 8:
                        if element not in subboards[2]:
                            subboards[2].append(element)
                        else:
                            return False
                    
                    if (index,element) not in coords:
                        coords.append((index,element))
                    else:
                        return False
                    clear_row.append(element)
            if len(set(clear_row)) != len(clear_row):
                return False

        return True

                   
                
            
