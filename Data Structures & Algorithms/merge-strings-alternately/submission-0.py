class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0,0
        n1,n2 = len(word1),len(word2)
        news = []
        while l < n1 and r < n2:
            news.append(word1[l])
            news.append(word2[r])
            l+=1
            r+=1
        while l < n1:
            news.append(word1[l])
            l+=1
        while r < n2 :
            news.append(word2[r])
            r +=1
        return ''.join(news)
            
