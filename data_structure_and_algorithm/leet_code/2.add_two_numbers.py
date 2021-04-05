"""
两数相加：

给两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
可以假设除了数字0之外，这两个数都不会以0开头。
例如：
1->3->4
2->4->5

431+542 = 973
返回
3->7->9

思路：
1. 创建一个新的链表cur，它的开头就是两个原始链表的头部之和。
2. 同时遍历两个链表，只要有一个没到头就一直遍历。如果有一个表为空了则补0节点
3. cur的每个值等于l1+l2+前一位的进位值。
4. 如果cur的尾部发生了进位，就再加一个节点。
时间复杂度O(n)，遍历完较长的链表就结束了。
空间复杂度O(max(m,n))，新加链表的长度为较长链表+1
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):

    head = ListNode(val=l1.val+l2.val)
    current = head
    while l1.next is not None or l2.next is not None:
        l1 = l1.next if l1.next is not None else ListNode()
        l2 = l2.next if l2.next is not None else ListNode()
        current.next = ListNode(val=l1.val + l2.val + current.val//10)
        current.val = current.val % 10
        current = current.next

    # 最后一位进位
    if current.val >= 10:
        current.next = ListNode(current.val//10)
        current.val = current.val % 10

    return head


l1 = ListNode(val=2)
l1.next = ListNode(val=2)
l1.next.next = ListNode(val=9)  # 正序922

l2 = ListNode(val=1)
l2.next = ListNode(val=2)
l2.next.next = ListNode(val=4)  # 正序421

result = add_two_numbers(l1, l2)
print(result.val, result.next.val, result.next.next.val, result.next.next.next.val)  # 正序1343
