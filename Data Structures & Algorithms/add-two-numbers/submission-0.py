# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2:
            val1,val2=0,0
            if l1:
                val1=l1.val
                l1=l1.next
            if l2:
                val2=l2.val
                l2=l2.next

            sumval=val1+val2
            # print(val1,val2,sumval,carry)
            if (sumval+carry)<10:
                curr.val=sumval+carry
                carry=0
            else:
                curr.val=((sumval+carry)%10)
                carry=1
            if l1 or l2 or carry:
                curr.next=ListNode()
                curr=curr.next
        if carry:
            curr.val=carry
        return dummy

            







        