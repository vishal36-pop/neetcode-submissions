class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def can_transform(w1,w2):
            #only one letter can 
            flag = False #turns True if encounterd a letter which is not same 
            ans = True
            for i in range(len(w2)):
                if w1[i] != w2[i] and flag == False:
                    flag = True
                    continue
                elif w1[i] != w2[i] and flag == True:
                    ans = False
            return ans
        #bfs
        q = collections.deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)
        #count to count the levels 
        count = 0
        #flag for the target found 
        flag = False
        while q :
            count+=1
            for _ in range(len(q)):
                u = q.popleft()
                for w in wordList:
                    if w not in visited and can_transform(u,w): #dont want to already visited because it simply forms a cycle and we just loop in that cycle and run into an inf loop
                        q.append(w)
                        visited.add(w)
                        if w == endWord:
                            flag = True
                            count+=1
                            break
                if flag == True:
                    break
            if flag == True:
                break
        return count if flag else 0
                


                

