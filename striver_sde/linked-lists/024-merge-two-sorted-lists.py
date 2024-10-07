from util import linkedlist, Node

def merge_two_lists(list1, list2):
    dummy = Node(-1)
    temp = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    
    if list1:
        temp.next = list1
    else:
        temp.next = list2

    return dummy.next

arr1 = [1,2,4]
arr2 = [1,3,4]
list1 = linkedlist(arr1)
list2 = linkedlist(arr2)
head = merge_two_lists(list1, list2)
print(head)
