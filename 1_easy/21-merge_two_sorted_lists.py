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

        while node1 or node2:
            if not node2 or node1.val < node2.val:
                new_list = ListNode(node1.val, new_list)
                node1 = node1.next
            else:
                new_list = ListNode(node2.val, new_list)
                node2 = node2.next
    
        return new_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node1 = list1
        node2 = list2
        new_list = []

        while node1 or node2:
            if node1 and (not node2 or node1.val < node2.val):
                new_list.append(ListNode(node1.val))
                node1 = node1.next
            else:
                new_list.append(ListNode(node2.val))
                node2 = node2.next
        
        if not new_list:
            return ListNode().next

        l = -2
        linked_list = new_list[-1]
        while l >= -len(new_list):
            new_list[l].next = linked_list
            linked_list = new_list[l]
            l -= 1
        return linked_list
    

# PERFORMANCE
# Runtime 44 ms (Beats 25.67% of users with Python)
# Memory 16.52 MB (Beats Beats 74.46% of users with Python)

if __name__ == '__main__':
    
    l1 = ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 4, next= None)))
    l2 = ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= None)))
    # assert Solution().mergeTwoLists(l1, l2) == ListNode(val= 1, next=
    #                                                     ListNode(val=1, next=
    #                                                              ListNode(val= 2, next=
    #                                                                       ListNode(val= 3, next= 
    #                                                                                ListNode(val=4, next=
    #                                                                                         ListNode(val=4, next= None))))))
    
    l1 = ListNode(val= 1)
    l2 = ListNode(val=2)
    assert Solution().mergeTwoLists(l1, l2) == ListNode(1, ListNode(2))
    