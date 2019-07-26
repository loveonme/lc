'''
这个简单，主要是能发现左右互换和对角线互换
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        dim = len(matrix)
        i = 0
        while i < dim -i -1:
            for j in range(dim):
                tmp = matrix[j][i] 
                matrix[j][i] = matrix[j][dim - i -1]
                matrix[j][dim - i -1] = tmp
            i += 1
        for i in range(dim):
            for j in range(dim - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[dim - j- 1][dim - i -1 ]
                matrix[dim - j- 1][dim - i -1 ] = tmp