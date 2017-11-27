#coding:utf-8
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
            思路：
                将flowerbed中1旁边的位置置位true.全部设置完之后，0的个数就是可以放花的最多数量
        """
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 1:
                if i != 0 and flowerbed[i-1] == 0:
                    flowerbed[i-1] = 2
                if i != length-1 and flowerbed[i+1] == 0:
                    flowerbed[i+1] = 2
        return flowerbed



if __name__ == '__main__':
    s = Solution()
    a = [1, 0, 0, 0, 1]
    print s.canPlaceFlowers(a, 2)

