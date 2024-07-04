from typing import List 

class ListNode():
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self, lis: List) -> None:
        self.head = self.array2List(lis)
    
    def array2List(self, lis: List) -> ListNode:
        if not lis:
            return None
        head = ListNode(lis[0])
        cur = head
        for ele in lis[1:]:
            cur.next = ListNode(ele)
            cur = cur.next
        return head
            
    def traversal(self, head: ListNode) -> List:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    def reverseWithLoop(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseWithRecursion(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        new_head = self.reverseWithRecursion(head.next)
        print(head.val)
        head.next.next = head
        head.next = None 
        return new_head


lis = [1,2,3,4,5,6]
linkedlis = LinkedList(lis)
print(linkedlis.traversal(linkedlis.head))
rev = linkedlis.reverseWithLoop(linkedlis.head)
print(linkedlis.traversal(rev))

rec = linkedlis.reverseWithRecursion(rev)
print(linkedlis.traversal(rec))

# 1->2->3->4->5->6