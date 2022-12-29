#Given an integer array nums sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. 

class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = list(set(nums))#creates list from array, set removes dupes
        nums.sort() #sorts numerically
        return len(nums) #return its length
