class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        #特殊情况考虑
        #z 为 0
        if z == 0:
            return True
        #z 大于 x y 之和 或者z 小于 0
        if z > x + y or z < 0:
            return False
        #z 等于x 或 y 
        if z in (x, y):
            return True
        
        #gcd
        a, b = x, y
        while a > 1 and b > 1:
            a, b = a % b, b % a
        #如果a b 有一个为0，说明x,y之间是倍数关系，那就看z是不是(a+b)的倍数，如果a, b中没有0，那么a, b就至少有一个1,有1就可以生成任何一个x,y之间的数
        if not a or not b:
            return z % (a + b) == 0 if (a + b)!=0 else False
        return True
