class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = 0
        ans = 0
        hashmap = collections.defaultdict(int)
        while r < len(fruits):
            hashmap[fruits[r]]+=1
            while len(hashmap) > 2:
                hashmap[fruits[l]] -=1
                if hashmap[fruits[l]] == 0:
                    del hashmap[fruits[l]]
                l+=1
            ans = max(ans,r-l+1)
            # print(l,r)
            r += 1
        return ans