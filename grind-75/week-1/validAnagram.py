"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
       
        # Contar as ocorrências de cada letra em 's'
        countS = {}
        for char in s:
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1
        
        # Contar as ocorrências de cada letra em 't'
        countT = {}
        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1
        
        # Comparar os dicionários de contagem
        return countS == countT
    
    
    def isAnagram_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s= sorted(s)
        t = sorted(t)

        return s==t
