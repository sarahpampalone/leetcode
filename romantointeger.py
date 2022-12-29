#Given a roman numeral, convert it to an integer

class Solution(object):
    def romanToInt(self, s):
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 
1000}
        result = 0
        for i in range(len(s) - 1):
            if num[s[i]] >= num[s[i + 1]]:
                result += num[s[i]]
            else:
                result -= num[s[i]]
        result += num[s[-1]]
        return result
