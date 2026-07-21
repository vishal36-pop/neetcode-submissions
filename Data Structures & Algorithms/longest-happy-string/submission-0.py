class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        trueset = set(('a','b','c'))
        freqmap = {'a':a,
                    'b':b,
                    'c':c
                    }
        queue = collections.deque([])
        heap = [(-f,c) for c,f in freqmap.items() if f>0]

        import heapq
        heapq.heapify(heap)
        t = 0
        s =''
        while heap:
            count,char = heapq.heappop(heap)
            if len(s)>1 and s[-1] == s[-2] == char:
                #this character cannot be added now 
                if not heap:
                    #and no other character cannot be added now
                    break
                #there is some other char which can be added
                count2,char2 = heapq.heappop(heap)
                s += char2
                count2+=1
                if count2 < 0:
                    heapq.heappush(heap,(count2,char2))
                #push the current char back
                heapq.heappush(heap,(count,char))
            else:
                s+=char
                count +=1
                if count < 0:
                    heapq.heappush(heap,(count,char))
        return s