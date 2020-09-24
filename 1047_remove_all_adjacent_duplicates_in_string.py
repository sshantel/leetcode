"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
"""

def removeDuplicates(S):

    stack = []
    for ch in S:
        if len(stack) > 0 and stack[-1] == ch:
            stack.pop()
        else: 
            stack.append(ch)

    return "".join(stack)
print(removeDuplicates('abbaca'))