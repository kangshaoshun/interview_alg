class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
            Time Compleity:O(N)
            Space Complexity:O(1)
            思路：这就是一道栈的应用题，学过数据结构的应该都知道
        """
        stack = []
        left = ['(', '{', '[']
        right = [')', '}', ']']
        for item in s:
            if item in left:
                stack.append(item)
            elif item in right:
                if not stack or stack[-1] != left[right.index(item)]:
                    return False
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
        
