class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW,COL= len(matrix),len(matrix[0])
        #COL= len(matrix[0])
        row0=False
        
        #determine which columns and rows needs to be zero
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r >0:
                        matrix[r][0]=0
                    else:
                        row0=True
        
        for r in range(1,ROW):
            for c in range(1,COL):
                if matrix[0][c]== 0 or matrix[r][0]==0:
                    matrix[r][c]=0
                    
        if matrix[0][0]==0: 
            for r in range(ROW):
                matrix[r][0]=0
                
        if row0:
            for c in range(COL):
                matrix[0][c]=0
        return matrix #if we wiil use it in leetcode remove return
                    
        