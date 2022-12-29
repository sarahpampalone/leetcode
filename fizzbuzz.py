class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ary = []
        for i in range(1, n+1):
            if i % 15 == 0:
                ary.append("FizzBuzz")
            elif i % 3 == 0:
                ary.append("Fizz")
            elif i % 5 == 0:
                ary.append("Buzz")
            else:
                ary.append(str(i))
        return ary
