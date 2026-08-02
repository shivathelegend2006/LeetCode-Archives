class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row*col - 1
        #just conduct bianry search with speacial rules ismple
        while l <= r:
            mid = (l+r)//2
            R = mid //col
            c = mid % col
            midVal = matrix[R][c]
            if midVal == target:
                return True
            elif midVal  < target:
                l = mid +1
            else:
                r = mid - 1

        return False