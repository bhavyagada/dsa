from util import linkedlist

def reverse_list(head):
    if not head: return head
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

head = linkedlist([1,2,3,4,5])
rev = reverse_list(head)
print(rev)
