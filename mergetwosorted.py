#You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

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
