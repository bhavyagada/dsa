from util import linkedlist

def remove_nth_from_end(head, n):
    slowp = head
    fastp = head
    for _ in range(n): fastp = fastp.next
    if not fastp: return head.next

    while fastp.next:
        slowp = slowp.next
        fastp = fastp.next
    slowp.next = slowp.next.next
    return head

arr = [1,2,3,4,5]
n = 2
head = linkedlist(arr)
ll = remove_nth_from_end(head, n)
print(ll)
