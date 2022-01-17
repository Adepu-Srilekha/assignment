class Solution:
    def countSegments(self, s: str) -> int:
        for x in "!@#$%^&*()_+-=',.:":
            s.replace(x," ")
        return len([x for x in s.split(" ") if x!= ""])
s='my name is srilekha'
obj=Solution()
result=obj.countSegments(s)
print(result) 