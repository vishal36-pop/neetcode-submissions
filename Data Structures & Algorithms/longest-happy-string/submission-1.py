class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq
        #freqmap 
        heap = [(-a,'a'),(-b,'b'),(-c,'c')]
        heap = [(f,al) for f,al in heap if f < 0]
        heapq.heapify(heap)
        ans = ''
        l = 0
        while heap:
            print(heap)
            f,al = heapq.heappop(heap)
            if l >=2 and ans[-1]==ans[-2]==al:
                #if heap then only possible else return ans
                if not heap:
                    return ans
                sf,sa = heapq.heappop(heap)
                ans+=sa
                l+=1
                if sf+1<0:
                    heapq.heappush(heap,(sf+1,sa))
                heapq.heappush(heap,(f,al))
                continue
            else:
                ans+=al
                l+=1
                if f+1<0:
                    heapq.heappush(heap,(f+1,al))
        return ans
                