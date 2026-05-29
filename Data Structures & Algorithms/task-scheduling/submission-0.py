class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counts = Counter(tasks)
        hashmap = [[-j, i] for i, j in counts.items()]
        import heapq
        heapq.heapify(hashmap)
        count = 0
        check = {i: -float('inf') for i in counts}
        popped = 0
        while popped != len(tasks):
            temp = []
            found = False
            while hashmap:
                a_count, a = heapq.heappop(hashmap)
                if count - check[a] > n:
                    check[a] = count
                    if a_count + 1 < 0:
                        heapq.heappush(hashmap, [a_count + 1, a])
                    popped += 1
                    found = True
                    break
                else:
                    temp.append([a_count, a])
            
            for item in temp:
                heapq.heappush(hashmap, item)
            
            count += 1
        return count