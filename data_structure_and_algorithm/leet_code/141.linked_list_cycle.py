"""
环形链表：
给定一个链表，判断链表中是否有环。

思路：
快慢指针
"""


def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:  # 二者相遇即确认有环，返回True
            return True
    return False