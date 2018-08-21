#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
实现乘方函数pow. 不得使用库函数
要求是实现一个高效，稳健的函数，考虑到各种情况
"""
def get_result(base, exp):
    if exp == 0:return 1
    if exp == 1:return base
    result = get_result(base, exp >> 1)
    result *= result
    if exp & 1:
        result *= base
    return result

"""
考虑以下几种情况：
    1.底数为0
        1）指数为0
        2）指数为正
        3）指数为负

    2.底数非0
        1）指数为0
        2）指数为正
        3）指数为负

    通用计算结果，采用 分治法节省时间
"""

def pow(base, exp):
    """
    :type base:float
    :type exp:int
    :rtype: float
    """
    if base == 0:
        if exp == 0:return 1
        elif exp > 0:return 0
        else: raise Exception('div zero')
    else:
        if exp == 0:return 1
        elif exp > 0:
            return get_result(base, exp)
        else:
            return 1.0/get_result(base, -exp)
