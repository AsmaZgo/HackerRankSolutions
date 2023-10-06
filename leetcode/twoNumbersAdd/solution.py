# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # For simplicity reasons we don't verify the constraints
        cur = 0
        res = ListNode()
        if l1 == None and l2 == None:
            return None

        if l1 <> None:
            cur = cur + l1.val
        if l2 <> None:
            cur = cur + l2.val
        res.val = cur % 10
        res.next = ListNode()
        res.next.val = cur / 10
        if l1 == None:
            self.addTwoNumbers_p(l1, l2.next, res.next)
        elif l2 == None:
            self.addTwoNumbers_p(l1.next, l2, res.next)
        else:
            if l1.next == None and l2.next == None and res.next.val == 0:
                res.next = None
            else:
                self.addTwoNumbers_p(l1.next, l2.next, res.next)
        return res

    def addTwoNumbers_p(self, l1, l2, curr):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = curr.val
        if l1 == None and l2 == None:
            curr = None

            return True

        if l1 <> None:
            cur = cur + l1.val
        if l2 <> None:
            cur = cur + l2.val
        curr.val = cur % 10

        curr.next = ListNode()
        curr.next.val = cur / 10

        if l1 == None:
            if l2.next == None and curr.next.val == 0:
                curr.next = None
            else:
                self.addTwoNumbers_p(l1, l2.next, curr.next)
        elif l2 == None:
            if l1.next == None and curr.next.val == 0:
                curr.next = None
            else:
                self.addTwoNumbers_p(l1.next, l2, curr.next)
        else:
            if l1.next == None and l2.next == None and curr.next.val == 0:
                curr.next = None
            else:
                self.addTwoNumbers_p(l1.next, l2.next, curr.next)
        return False
