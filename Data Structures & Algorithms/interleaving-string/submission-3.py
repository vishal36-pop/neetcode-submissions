class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if len(s1) + len(s2) != len(s3):
        #     return False
        def ans(s1,s2):
            i = 1
            l = 0
            r = 0
            k = 0
            ans = True
            while k < len(s3)  :
                print(f'i:{i}')
                if i % 2 :
                    if l >= len(s1):
                        ans = False
                        break
                    if l< len(s1) and s3[k] != s1[l]:
                        ans = False
                        break
                    print(k)
                    while k < len(s3) and l < len(s1) and s3[k] == s1[l] :
                        k+=1
                        l+=1
                    else:
                        i+=1
                        continue
                else:
                    if r >= len(s2):
                        ans = False
                        break
                    if r < len(s2) and s3[k] != s2[r]:
                        ans = False
                        break
                    while k < len(s3) and r < len(s2) and s3[k] == s2[r] :
                        k+=1
                        r+=1
                    else:
                        i+=1
                        continue
            if k == len(s3) and (r<len(s2) or l<len(s1)):
                ans = False
            return ans
        return ans(s1,s2) or ans(s2,s1)