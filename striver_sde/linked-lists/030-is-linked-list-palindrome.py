from util import linkedlist

def reverse_second_half(head):
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

def is_palindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    rev_head = reverse_second_half(slow)
    rev = rev_head
    temp = head
    while rev:
        if rev.val != temp.val: return False
        rev = rev.next
        temp = temp.next
    return True

arr = [1,2,3,2,1]
head = linkedlist(arr)
ans = is_palindrome(head)
print(ans)
assert ans == True