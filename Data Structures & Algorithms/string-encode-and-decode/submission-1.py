class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string+= str(len(i))+"#"+i

        # print(string)
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i<len(s):
            j=i
            while j<len(s) and s[j]!="#":
                j+=1
            length = int(s[i:j]) # lenght of upcoming word
            j+=1
            res.append(s[j:j+length])# append whole of word
            i = j+length


        return res
