/*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.*/

class Solution(object) :
  def twoSum(self, nums, target) :
    d = {}
    for i, n in enumerate(nums) :
      m = target - n
      if m in d :
        return [d[m], i]
      else :
        d[n] = i
