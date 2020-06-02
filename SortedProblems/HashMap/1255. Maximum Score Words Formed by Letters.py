"""
Given a list of words, list of single letters (might be repeating) and score of every character.
Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 
'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

EXAMPLE 1: 
    Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    Output: 23
    Explanation:
    Score  a=1, c=9, d=5, g=3, o=2
    Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
    Words "dad" and "dog" only get a score of 21.

CONSTRAINTS:
    1 <= words.length <= 14
    1 <= words[i].length <= 15
    1 <= letters.length <= 100
    letters[i].length == 1
    score.length == 26
    0 <= score[i] <= 10
    words[i], letters[i] contains only lower case English letters.
"""

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        ch_score = dict(zip(string.ascii_lowercase, score))
        word_scores = [sum([ch_score[ch] for ch in word]) for word in words]
        word_counts = [collections.Counter(word) for word in words]
        
        self.score = 0
        def check_path(word_index, letters, path_score):
            if word_index == len(words): 
                self.score = max(self.score, path_score)
                return
            
            include_cur = True
            for k,v in word_counts[word_index].items():
                if v > letters[k]:
                    include_cur = False
                letters[k] -= v
                
            if include_cur:
                check_path(word_index + 1, letters, path_score + word_scores[word_index])
            
            for k,v in word_counts[word_index].items():
                letters[k] += v
            check_path(word_index + 1, letters, path_score)

        check_path(0, collections.Counter(letters), 0)
        return self.score
