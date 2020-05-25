# attempt
class Solution:
    def isValid(self, s: str) -> bool:
        if s == '': return True
        # inner brackets must be closed before outer ones
        # same number of opening and closing brackets of same type
        mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }
        open_brackets = ['(', '[', '{']
        stack = []
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            elif stack:
                prev = stack.pop()
                if mapping[prev] != bracket:
                    return False
            else:
                return False
        return stack == []

# optimal
class Solution(object):
    def isValid(self, s):
        # The stack to keep track of opening brackets.
        stack = []
        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}
        # For every bracket in the expression.
        for char in s:
            # If the character is an closing bracket
            if char in mapping:
                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'
                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)
        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

# same idea, but instead of having an explicit list for open brackets, it checks for open brackets using the hashmap
# uses the idea that if it is closing bracket, the previous element must be its corresponding opening bracket
# and using the dummy value takes care of cases where the stack is empty but a closing bracket was found
