"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

>>> deleteDuplicates(1 -> 1 -> 2)
1->2

>>> deleteDuplicates(1 -> 1 -> 2 -> 3 -> 3)
1 -> 2 -> 3

"""

def deleteDuplicates(head):
    current = head
    while head != None and current.next != None: 
        if current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')