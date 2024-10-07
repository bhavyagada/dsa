from util import Node

def find_intersection(headA, headB):
    d1 = headA
    d2 = headB
    while d1 != d2:
        d1 = headB if d1 == None else d1.next
        d2 = headA if d2 == None else d2.next
    return d1

# setup linked list
headA = Node(1)
headA.next = Node(2)
headA.next.next = Node(3)
headB = Node(10)
headB.next = Node(20)
headB.next.next = Node(30)
headB.next.next.next = headA.next.next
headA.next.next.next = Node(4)
headA.next.next.next.next = Node(5)
headA.next.next.next.next.next = Node(6)

ans = find_intersection(headA, headB)
print(ans)
