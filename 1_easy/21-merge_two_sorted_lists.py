from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        new_list = ListNode(0)
        
        # first = ListNode(1)
        # second = ListNode(2)
        # third = ListNode(3)
        # forth = ListNode(4)
        # first.next = second
        # second.next = third
        # third.next = forth
        # forth.next = None

        while node1 or node2:
            if not node2 or node1.val < node2.val:
                new_list = ListNode(node1.val, new_list)
                node1 = node1.next
            else:
                new_list = ListNode(node2.val, new_list)
                node2 = node2.next
    
        return new_list
    
    
if __name__ == '__main__':
    
    l1 = ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 4, next= None)))
    l2 = ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= None)))
    assert Solution().mergeTwoLists(l1, l2) == ListNode(val= 1, next=
                                                        ListNode(val=1, next=
                                                                 ListNode(val= 2, next=
                                                                          ListNode(val= 3, next= 
                                                                                   ListNode(val=4, next=
                                                                                            ListNode(val=4, next= None))))))
    