EXPLANATION:-
   The idea behind this solution is we have only access to node to be deleted.
   So, copy the contents of next node and delete the next node.
   
   time:- O(1)
   space:- O(1)
   
 IF YOU WANT SOLUTION IN JAVA, THEN VISIT HERE:( https://github.com/GHATAK123/June-LeetCode-Challenge./blob/master/delete_node_in_singly_linked_List_june_2.java )
   
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
