from util import linkedlist

def rotate_right(head, k):
    if not head or k == 0: return head
    length = 1
    temp = head
    while temp.next:
        length += 1
        temp = temp.next
    k = k % length
    end = length - k
    temp.next = head
    while end:
        end -= 1
        temp = temp.next
    head = temp.next
    temp.next = None
    return head

arr = [1,2,3,4,5]
k = 2
head = linkedlist(arr)
ans = rotate_right(head, k)
print(ans)