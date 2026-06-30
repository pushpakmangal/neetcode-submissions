class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        row_l,row_r=0,rows-1
        col_l,col_r=0,cols-1

        if matrix[0][0]>target or matrix[row_r][col_r]<target:
            return False

        while row_l<=row_r and col_l<=col_r:
            mid_row=row_l+(row_r-row_l)//2
            mid_col=col_l+(col_r-col_l)//2
            print(row_l, row_r, mid_row, col_l, col_r, mid_col)
            if matrix[mid_row][mid_col]==target:
                return True

            elif matrix[mid_row][mid_col]<target:
                if matrix[mid_row][col_r]<target:
                    row_l=mid_row+1
                else:
                    row_l=mid_row
                    row_r=mid_row
                    col_l=mid_col+1
            else:
                if matrix[mid_row][col_l]>target:
                    row_r=mid_row-1
                else:
                    row_l=mid_row
                    row_r=mid_row
                    col_r=mid_col-1
             

        return False



        