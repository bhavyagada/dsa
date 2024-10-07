class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"Node(val={self.val}, next={self.next})"

def linkedlist(arr):
    head = Node(arr[0])
    current = head

    for i in arr[1:]:
        current.next = Node(i)
        current = current.next
    return head
