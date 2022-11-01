#Time Complexity:: O(n^3)-traversing list of words multiple times
#Space Complexity:: O(n)-Recursive Stack Space-max length of RS is length of list
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        m=len(wordList[0]) # assigning length of wordlist to m
        wordList = set(wordList) #pushing the wordlist into a set
        
        wordList.add(beginWord) #adding the begin word to the set also
        
        adj = defaultdict(list) # creating a defaultdict to store the words
        for word in wordList: #each word in the wordlist gets processed into a similar string and appended into the adjacency matrix
            for i in range(m):
                s = word[:i] + "_" + word[i+1:]
                adj[s].append(word)
                
        q=deque() #creating queue
        q.append(beginWord) #appending beginword to queue
        visited = set() #creating visited set
        dist = 0 #assigning dist to 0
        visited.add(beginWord) #adding beginword in visited
        while q:
            dist += 1 #increment dist by 1
            size = len(q)
            
            for _ in range(size):
                currWord = q.popleft() #popping from queue
                
                for i in range(m):
                    s = currWord[:i] + "_" + currWord[i+1:] #creating _ string to identify patterns
                    
                    for nextWord in adj[s]: #match with every word in adjacency matrix
                        visited.add(nextWord) #adding the word in visited array
                        q.append(nextWord) # appending the word in visited
                        
                        if nextWord == endWord: #if nextword is equal to endword
                            return dist+1 
                        
        return 0