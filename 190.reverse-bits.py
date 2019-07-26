class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bit_arr = []
        num = n
        while num != 0:
            bit_arr.append(num - (num / 2)*2)
            num /= 2
        while len(bit_arr) < 32:
            bit_arr.append(0)
        print bit_arr
        i = 0
        res = 0
        while i < len(bit_arr):
            res = res*2 +bit_arr[i]
            i += 1
        return res
