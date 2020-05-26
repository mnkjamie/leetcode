# attempt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        multiplier = 1
        while l1:
            num1 += l1.val * multiplier
            l1 = l1.next
            multiplier *= 10
        multiplier = 1
        while l2:
            num2 += l2.val * multiplier
            l2 = l2.next
            multiplier *= 10
        summed = str(num1 + num2)[::-1]
        summed_list = ListNode()
        head = summed_list
        for idx in range(len(summed)):
            summed_list.val = int(summed[idx])
            print(summed_list.val)
            if idx == len(summed) - 1:
                break
            summed_list.next = ListNode()
            summed_list = summed_list.next
        return head

# optimal
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next

# I actually thought about this idea while coding through my attempt after noticing that at each position I could just add the same position from the two lists
# faster as it does not need to carry out conversions
