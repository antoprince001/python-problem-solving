# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Brute force solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None and list2 == None):
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
    
        if list1.val <= list2.val:
            start = ListNode(list1.val,None)
            sorted_list = start
            list1 = list1.next
        else:
            start = ListNode(list2.val,None)
            sorted_list = start
            list2 = list2.next

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                sorted_list.next = ListNode(list1.val,None)
                sorted_list = sorted_list.next
                list1 = list1.next
            else:
                sorted_list.next = ListNode(list2.val,None)
                sorted_list = sorted_list.next
                list2 = list2.next
        
        while list1 != None:
            sorted_list.next = ListNode(list1.val,None)
            sorted_list = sorted_list.next
            list1 = list1.next
        
        while list2 != None:
            sorted_list.next = ListNode(list2.val,None)
            sorted_list = sorted_list.next
            list2 = list2.next
        print(start)
        return start

# Better solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None and list2 == None):
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
    
        start = ListNode()
        sorted_list = start

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                sorted_list.next = list1
                list1 = list1.next
            else:
                sorted_list.next = list2
                list2 = list2.next
            sorted_list = sorted_list.next

        sorted_list.next= list1 or list2

        return start.next
