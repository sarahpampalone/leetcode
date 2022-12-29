/* Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string “” */

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        curr = head = ListNode()
        while list1 and list2:
            if (list1.val <= list2.val):
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        if list1 or list2:
            curr.next = list1 if list1 else list2
        return head.next
