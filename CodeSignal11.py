def reverseParentheses(s):
    for i in range(s.count('(')):
        index_paren = s.find(')')
        substring = ''

        while s[index_paren] != '(':
            substring += s[index_paren]
            index_paren -= 1

        s = s[:index_paren] + substring[1:] + s[s.find(')')+1:]
    return(s)

"""
You have a string s that consists of English letters, punctuation marks, 
whitespace characters, and brackets. It is guaranteed that the parentheses 
in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching 
parentheses, starting from the innermost pair. The results string should 
not contain any parentheses.

Example

For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".
"""

s = "abc(cba)ab(bac)c"
if __name__ == '__main__':
    reverseParentheses(s)
