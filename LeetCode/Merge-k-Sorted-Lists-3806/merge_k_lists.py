import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    h = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(h, (lst.val, i, lst))
    
    dummy = ListNode(0)
    curr = dummy
    while h:
        val, i, node = heapq.heappop(h)
        curr.next = ListNode(val)
        curr = curr.next
        if node.next:
            heapq.heappush(h, (node.next.val, i, node.next))
    return dummy.next
