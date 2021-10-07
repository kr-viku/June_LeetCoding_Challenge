class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        k=max(indices)
        res=[0]*(k+1)
        for i in range(len(s)):
            res[indices[i]]=s[i]
        ans="".join(res)
        return ans
