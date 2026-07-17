class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def next_states(state:str):
            next_states = []
            for i in range(len(state)):
                #increase 
                if state[i] != '9':
                    next_states.append(state[:i]+str(int(state[i])+1)+state[i+1:])
                else:
                    next_states.append(state[:i]+'0'+state[i+1:])
                #decrease
                if state[i] != '0':
                    next_states.append(state[:i]+str(int(state[i])-1)+state[i+1:])
                else:
                    next_states.append(state[:i]+'9'+state[i+1:])
            return next_states
        
        #now initialize a queue 
        q = collections.deque()
        q.append('0000')
        visited = set()
        visited.add('0000')
        #a hashset for teh deadends:
        deadends = set(deadends)
        #counter 
        count = 0 
        if target == '0000' or ('0000' in deadends):
            return -1
        #target flag
        flag = False
        while q :
            count+=1
            for _ in range(len(q)):
                currstate = q.popleft()
                for nex_s in next_states(currstate):
                    if nex_s not in deadends and nex_s not in visited:
                        q.append(nex_s)
                        visited.add(nex_s)
                        if nex_s == target:
                            flag = True
                            break
                if flag == True:
                    break
            if flag == True:
                break
        return count if flag else -1



                        