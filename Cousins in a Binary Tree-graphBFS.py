#Time Complexity:: O(n)-all nodes are visited in each level and Null values are also process
#Space Complexity:: O(n)-a list is used at each level, in this case usually less than O(n) as each level has a root element not included in list
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = deque() #create a queue
        q.append(root) #push root node into queue
        
        while q:
            size = len(q) #find the size of the queue
            level = set() #create a set to store the x and y of the node
            
            for _ in range(size): #for each node in the queue
                node = q.popleft() #pop the node
                level.add(node.val) #add the node to the level
                
                if node.left and node.right and ((node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x)):
                    return False #if the x and y aren't cousins then return False
                if node.left:
                    q.append(node.left) #if the left node not null then add to queue
                if node.right:
                    q.append(node.right) #if the right node not null then add to queue
            if x in level and y in level: #if x and y are in same level they are cousins
                return True
        return False #if there are no cousins detected then return