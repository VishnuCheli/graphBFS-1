#Graph
#Time Complexity:: O(n)-all nodes are visited in each level and Null values are also process
#Space Complexity:: O(n)-a list is used at each level, in this case usually less than O(n) as each level has a root element not included in list
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        self.graph = defaultdict(set) #creating a graph using hash set with all nodes in traversing branch
        self.visited = set() #a hashset to traverse all the nodes
        
        self.dfs(root, target.val) #passing the root node into a dfs
        result = [target.val]
        
        for i in range(k):
            size=len(result)
            level = []
            for j in range(size):
                curr = result.pop() #pop out 
                if curr not in self.visited: #if the current node is not already in visited nodes
                    level += self.graph.get(curr, [])
                    self.visited.add(curr) #adding current node to visited node
            result = level 
            
        finalResult = []
        for value in result:
            if value not in self.visited:
                finalResult.append(value)
                    
        return finalResult #returning the list of nodes that are k distance away from target
            
    
    def dfs(self, root, target):
        if not root: #base case
            return
        
        #logic
        if root.left: #if root.left not null, then traversing all the left branches and adding the nodes in the path
            self.graph[root.val].add(root.left.val) 
            self.graph[root.left.val].add(root.val)
            self.dfs(root.left, target)
            
        if root.right: #if root.right not null, then traversing all the right branches and adding the nodes in the path
            self.graph[root.val].add(root.right.val)
            self.graph[root.right.val].add(root.val)
            self.dfs(root.right, target)