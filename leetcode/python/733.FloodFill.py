#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        def modifyImage(image, i, j, oldColor, newColor):
            if i >= 0 and i < rows and j >= 0 and j < cols \
                    and image[i][j] == oldColor:
                        image[i][j] = newColor
                        modifyImage(image, i + 1, j, oldColor, newColor)
                        modifyImage(image, i - 1, j, oldColor, newColor)
                        modifyImage(image, i, j + 1, oldColor, newColor)
                        modifyImage(image, i, j - 1, oldColor, newColor)
        oldColor = image[sr][sc]
        if oldColor != newColor:
            modifyImage(image, sr, sc, oldColor, newColor)
        return image

if __name__ == '__main__':
    s = Solution()
    image = [[0, 0, 0], [0, 1, 1]]
    print s.floodFill(image, 1, 1, 1)

