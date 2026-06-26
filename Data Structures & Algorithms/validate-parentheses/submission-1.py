class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) > 1:
                if (stack[-1] == "]" and stack[-2] == "[") or (stack[-1] == "}" and stack[-2] == "{") or (stack[-1] == ")" and stack[-2] == "("):
                    stack.pop()
                    stack.pop()
                    
        
        return stack == []