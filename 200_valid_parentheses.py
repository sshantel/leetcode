"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

""" 
def isValid(s):
        #create hashmap of the matching brackets as key, value pairs
        #create list of open brackets only
        #loop through each bracket in s
        #create a stack
        #if the character is an open character: append it to the stack 
        #elif the stack isnt empty and the letter is matching the pair to the hashmap
        #else return false
        #return stack == []
        
        map_brackets = {'(':')', '{':'}', '[':']'}
        open_brackets = ['(', '[', '{']
        stack = []
        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif stack and i == map_brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
print(isValid("()"))
print(isValid("()"))