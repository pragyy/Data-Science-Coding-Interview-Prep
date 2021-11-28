"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        array = []
        for ll in lists:
			while ll:
				array.append(ll.val)
				ll = ll.next

        
        array.sort()
        
        if array != []:
            self.head = ListNode()
            self.temp = self.head
            for num in array:
                self.temp.next = ListNode(num)
                self.temp = self.temp.next
            return self.head.next

"""
Time Complexity - O(nk)
Space Complexity - O(n)
"""
