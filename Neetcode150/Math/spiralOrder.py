# https://leetcode.com/problems/spiral-matrix/description/
"""
Spiral : Top, Bottom, Left, Right pointers
Base Case : if top == bottom or left == right
[1,2,3,4
5,6,7,8
9,10,11,12]
: 1,2,3,4,8,12,11,10,9 :: now new array : [5,6,7,8] : new rectangle (shift top to down and increment left) :: Do for all.
Only tricky part : right and bottom are placed at right + 1 and bottom + 1 (to make things easier (draw to visualise))

Input : [[1,2,3],[4,5,6],[7,8,9]]
Output : [1,2,3,6,9,8,7,4,5]

Time : O(m * n), Space : O(1)
"""


class Solution:
    def spiralOrder(matrix):
        ans = []
        # right and bottom = set out of bounds bcs of for loop
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            # left -> right : get every value (i) in the top row
            for i in range(left, right):
                ans.append(matrix[top][i])  # row remains same
            top += 1  # shifting top down by 1

            # top -> bottom get every value (i) in right column
            for i in range(top, bottom):
                # right is out of bounds : subtract 1
                ans.append(matrix[i][right - 1])
            right -= 1  # all done : decrement right

            # Edge Cases
            # [1, 2, 3] or [1,
            #               2,
            #               3]
            if not (left < right and top < bottom):
                break

            # bottom row (right -> left)
            for i in range(right - 1, left - 1, -1):  # left is non-inclusive
                # bottom is also out of bounds initially
                ans.append(matrix[bottom - 1][i])
            bottom -= 1  # shift it upwards

            # get every i in the left most col (bottom to top)
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1  # shift it to right

        return ans


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution.spiralOrder(matrix))
