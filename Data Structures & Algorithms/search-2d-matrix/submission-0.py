class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def col_bin(matrix, target):
            n = len(matrix)
            start, end = 0, n - 1
            while start <= end:
                mid = (start + end) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif matrix[mid][-1] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1  

        def binsearch(row_no, target):
            if row_no == -1:
                return False
            row = matrix[row_no]
            start, end = 0, len(row) - 1
            while start <= end:
                mid = (start + end) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return False

        row_no = col_bin(matrix, target)
        return binsearch(row_no, target)



        