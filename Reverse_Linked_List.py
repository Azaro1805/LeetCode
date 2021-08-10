# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if(head == None):
            return head 
        if(head.next == None):
            return head 
        current = head 
        nextN = head. next
        head.next =  None
        
        while nextN : 
            temp = nextN.next
            nextN.next =  current 
            current = nextN 
            if (temp == None):
                break
            nextN = temp
        return nextN
        