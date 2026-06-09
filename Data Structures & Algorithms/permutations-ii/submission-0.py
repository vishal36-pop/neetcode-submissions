class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        path = []
        #hashmap
        counter = collections.Counter(nums)
        print(counter)
        used = [False for _ in range(l)]
        def backtrack(path):
            if len(path) == l:
                ans.append(path[:])
                return 
            print(path,used)
            for i in counter:
                if counter[i]<=0:
                    continue
                #backtrack
                path.append(i)
                counter[i]-=1
                backtrack(path)
                path.pop()
                counter[i]+=1
        backtrack(path)
        return ans