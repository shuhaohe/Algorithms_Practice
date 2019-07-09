class Solution(object):
    def __init__(self, *args, **kwargs):
        self.record = {
            0:1,
            1:1,
            2:2
        }
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return None
        if n in self.record:
            return self.record.get(n)
        
        sum = 0 
        for i in range(1, n+1):
            sum += self.numTrees(i-1) * self.numTrees(n-i)
        
        self.record[n] = sum
        return sum


if __name__ == "__main__":
    n = 5
    s = Solution()
    print(s.numTrees(n))