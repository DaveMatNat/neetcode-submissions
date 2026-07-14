class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find which row would have the element
        rows, cols = len(matrix), len(matrix[0])

        # perform binary search on the first elements of each row to find the row that might have the element
        l,r = 0, rows-1

        possible_row = -1

        # log m time
        while l <= r:
            mid = (l+r)//2

            # using mid row's 1st and last element as a decider

            if target > matrix[mid][-1]: # target > the mid row's last element
                l = mid + 1
            elif target < matrix[mid][0]: # target < the mid row's first element
                r = mid - 1
            else: # otherwise the target must be within the mid row
                possible_row = mid
                break 
        
        # log n time

        # find element in the row
        l,r = 0, cols-1
        while l <= r:
            mid = (l+r)//2
            if matrix[possible_row][mid] == target:
                return True
            elif matrix[possible_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

        # total runtime -> log m + log n -> log(m*n)