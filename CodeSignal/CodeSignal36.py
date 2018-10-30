import re
def longestWord(text):
    words = re.compile('[a-zA-Z]+').findall(text)
    return max(words, key=len)

"""
Define a word as a sequence of consecutive English letters. 
Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".
"""

text = "Ready, steady, go!"
if __name__ == '__main__':
    print(longestWord(text))
