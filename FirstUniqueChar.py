'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_dict = {}
        for c in s:
            if c in char_dict.keys():
                char_dict[c] = char_dict[c] + 1
            else:
                char_dict[c] = 1

        idx = 0
        for x in char_dict:
            if char_dict[x] == 1:
                return idx
            idx = idx + 1

        return -1


s = Solution()
print("leetcode: ", s.firstUniqChar("leetcode"))
print("loveleetcode: ", s.firstUniqChar("loveleetcode"))
print("aabb: ", s.firstUniqChar("aabb"))

