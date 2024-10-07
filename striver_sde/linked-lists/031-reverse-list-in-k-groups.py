from util import linkedlist

def reverse_k_nodes(head):
    temp = head
    prev = None
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

def get_kth_node(temp, k):
    k -= 1
    while temp and k > 0:
        k -= 1
        temp = temp.next
    return temp

def reverse_k_groups(head, k):
    temp = head
    prev_last = None
    while temp:
        kth_node = get_kth_node(temp, k)
        if not kth_node:
            if prev_last:
                prev_last.next = temp
            break

        next_node = kth_node.next
        kth_node.next = None
        reverse_k_nodes(temp)
        if temp == head:
            head = kth_node
        else:
            prev_last.next = kth_node

        prev_last = temp
        temp = next_node
    return head

arr = [1,2,3,4,5,6,7,8,9,10]
head = linkedlist(arr)
ans = reverse_k_groups(head, 3)
print(ans)
