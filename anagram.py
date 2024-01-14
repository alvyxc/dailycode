'''You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
 

Constraints:

1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.'''


class Solution(object):
    @staticmethod
    def min_steps(s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        base_index = ord('a')
        buckets = [0] * 26
        for c in s:
            buckets[ord(c) - base_index] += 1

        for c in t:
            buckets[ord(c) - base_index] -= 1

        answer = 0
        for i in buckets:
            if i < 0:
                answer += i * -1

        return answer


step = Solution.min_steps("bab", "aba")
print("step is ", step)

step = Solution.min_steps("leetcode", "practice")
print("step is ", step)

step = Solution.min_steps("anagram", "mangaar")
print("step is ", step)
