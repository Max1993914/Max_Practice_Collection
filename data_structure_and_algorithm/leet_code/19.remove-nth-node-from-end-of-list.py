"""
删除链表中倒数第k个节点，返回头节点。一次遍历实现。
例如输入：1->3->4->5 k=2
输出：1->3->5

思路：双指针
当我们需要删除节点x时，需要知道它的前驱节点x-1。并使得x-1.的指针指向x的下一个节点来达到删除的目的。
由于头节点没有前驱节点，如果删除头节点需要做特殊处理，这里加一个哨兵节点在前面，使慢指针指向它，快指针指向头节点。
1. 首先快节点向前移动n次，此时慢节点与快节点之间的距离为n+1（由于哨兵所以+1）
2. 一起推进快慢节点，当快节点变成None的时候，慢节点即为待删除节点的前驱节点。
3. 前驱节点链接待删除节点的下一个节点，达到删除的目的。
4. 返回哨兵节点.next，而不是head，因为head有可能被删除
时间复杂度：O(n)
空间复杂度：O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    dum = ListNode(0, head)  # 哨兵节点，解决头节点需要特殊处理的问题
    slow = dum
    fast = head

    for i in range(n):
        fast = fast.next

    while fast is not None:  # 当fast变成none时，slow成为了待删除节点的前驱节点。
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dum.next

