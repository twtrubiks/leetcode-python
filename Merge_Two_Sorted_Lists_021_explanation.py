from Merge_Two_Sorted_Lists_021 import ListNode

if __name__ == "__main__":
    a = b = 3
    c = 3
    print('a', id(a))
    print('b', id(b))
    print('c', id(c))
    b = 4
    print('a', id(a))
    print('b', id(b))
    print('a', a)
    print('b', b)

    L1 = L2 = ListNode(0)
    L3 = ListNode(0)
    print('L1', id(L1))
    print('L2', id(L2))
    print('L3', id(L3))
    print('L1 == L2', L1 == L2)
    print('L1 is L2', L1 is L2)
    print('L1 == L3', L1 == L3)
    print('L1 is L3', L1 is L3)
    L2.next = ListNode(1)
    print("see L1 and L2 var")
    L2 = L2.next
    print("see L1 and L2 var")
    L2.next = ListNode(2)
    print("see L1 and L2 var")

