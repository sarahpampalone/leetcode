# Given an integer x, return true if x is a palindrome, and false otherwise

class Solution(object) :
  def isPalindrome(self, x) :
    str_x = str(x)
    if str_x == str_x[::-1]:
      return True
    else
      return False
