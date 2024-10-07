from util import linkedlist

def middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

arr = [1,2,3,4,5,6]
head = linkedlist(arr)
mid = middle_node(head)
print(mid)
