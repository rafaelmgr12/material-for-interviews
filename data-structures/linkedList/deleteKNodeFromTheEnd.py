# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        len_p = head
        temp = head
        length = 0
        while len_p:
            length+=1
            len_p = len_p.next
        if length == n:
            head = head.next
            return head
        count = 1
        while count < length-n:
            count += 1
            temp = temp.next
        temp.next = temp.next.next
        
        return head