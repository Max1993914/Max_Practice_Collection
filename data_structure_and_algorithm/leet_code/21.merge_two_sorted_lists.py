"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

思路：
类似于归并排序，两个链表一起遍历，将较小值拼到新链表上。最后把没有遍历完的链表放在最后面。
使用一个哨兵使得操作更简便，不用对空链表做特殊处理。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):
    dum = ListNode()
    pre = dum
    while l1 and l2:
        if l1.val < l2.val:
            pre.next = l1
            l1 = l1.next
        else:
            pre.next = l2
            l2 = l2.next
        pre = pre.next

    if l1:
        pre.next = l1

    if l2:
        pre.next = l2

    return dum.next
