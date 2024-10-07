from util import linkedlist, Node

def add_two_numbers(l1, l2):
    dummy = Node(-1)
    temp = dummy
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        sum += carry
        carry = sum // 10
        node = Node(sum % 10)
        temp.next = node
        temp = temp.next
    return dummy.next

arr1 = [9,9,9,9,9]
arr2 = [9,9,9]
l1 = linkedlist(arr1)
l2 = linkedlist(arr2)
ans = add_two_numbers(l1, l2)
print(ans)