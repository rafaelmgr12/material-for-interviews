# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = None
            
        if list1 is None:
            return list2
        elif list2 is None:
            return list1 
        
        if list1.val < list2.val:
            result = list1
            result.next = self.mergeTwoLists(list1.next,list2)
        else:
            result = list2
            result.next = self.mergeTwoLists(list1,list2.next)
        return result
        
#         while (list1 and list2):
#             if (list1.val < list2.val ):
#                 new_list.next = list1
#                 list1 = list1.next
#             else:
#                 new_list.next = list2
#                 list2 = list2.next
#             new_list = new_list.next
        
#         new_list.next = list1 or list2
#         return head.next