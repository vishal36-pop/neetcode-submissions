class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        #here we should find the minimum distance to the target 
        #when the nei = target
        source = ['0000']
        deadends = set(deadends)
        visited = set()
        visited.add('0000')
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0
        queue = collections.deque(source)
        
        l = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                for i in range(4):
                    digit = int(curr[i])
                    for d in (1,-1):
                        new_digit = str((digit+d)%10)
                        new_state = curr[:i]+new_digit+curr[i+1:]
                        if new_state in deadends:
                            continue
                        if new_state not in visited:
                            if new_state == target:
                                return l+1
                            visited.add(new_state)
                            queue.append(new_state)
            l+=1
        return -1