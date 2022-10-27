class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")":"(", "]":"[", "}":"{" }  # map the closing element to opening one
        
        for c in s:                              #going thru every character in the string
            if c in closeToOpen:         # checking if the character is closing paranthesis
                if stack and stack[-1] == closeToOpen[c]:  #stack -1 is the last value we added to the stack,           we wanna make sure that our stack is not empty before adding a closing parenthesis, and check if it matches
                    stack.pop()    # removes the element that equals to closeToOpen c 
                else:
                    return False   
            else:
                stack.append(c)
        
        return True if not stack else False  # If not stack (if the stack is empty) it means every pair had its match, so we return True. If there's still something in the stack, it means there are still brackets left to close, so we return False
                
            
            
            
            # O(n) because we only have to go thru every input character once
            # O(n) memory because we are using a stack