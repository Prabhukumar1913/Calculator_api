# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         slow=head
#         fast=head
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#             return True
#         return False

# obj=Solution()
# print(obj.hasCycle([3,2,0,-4]))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Create linked list:
# 3 → 2 → 0 → -4
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4

# Create cycle:
# -4 → 2
node4.next = node2


# Test
obj = Solution()

print(obj.hasCycle(node3))