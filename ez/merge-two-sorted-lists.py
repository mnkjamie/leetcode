# attempt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None: return None
        merged = ListNode()
        head = merged
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                merged.val = l1.val
                l1 = l1.next
            else:
                merged.val = l2.val
                l2 = l2.next
            merged.next = ListNode()
            merged = merged.next
        if l1 == None:
            while l2 != None:
                merged.val = l2.val
                l2 = l2.next
                if l2 == None:
                    break
                merged.next = ListNode()
                merged = merged.next
        else:
            while l1 != None:
                merged.val = l1.val
                l1 = l1.next
                if l1 == None:
                    break
                merged.next = ListNode()
                merged = merged.next
        return head

# optimal
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

# remember to account for empty cases and ending values if appending to answer
# I didn't have to iterate through the rest of one list once one list was finished, careless mistake
# also didn't have to instantiate new ListNodes every time if done the way above, just use l1 and l2 and change if necessary

# recursive solution
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# personally like this recursive solution the best, very intuitive
