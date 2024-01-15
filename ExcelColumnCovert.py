'''Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

26 + 2
A * 26 + B

Input: columnNumber = 701
Output: "ZY"
26 * 26 + 25

Input: columnNumber = 731
Output: "ABC"

1 * 26 * 26 + 2 * 26 + 3 = 731

Constraints:

1 <= columnNumber <= 231 - 1'''


class Solution2(object):
    @staticmethod
    def convert_to_title(column_number):
        """
        :type column_number: int
        :rtype: str
        """

        column_str = ""
        while column_number > 0:
            rem = column_number % 26
            print("rem is ", rem)
            if rem == 0:
                column_str += 'Z'
                column_number = column_number // 26 - 1
            else:
                column_str += chr(64 + rem)
                column_number = (column_number - rem) // 26

        return column_str[::-1]


class Solution(object):
    @staticmethod
    def convert_to_title(column_number):
        """
        :type column_number: int
        :rtype: str
        """

        # find number of digits
        largest_number = 2**31 - 1
        num_digits = 1
        largest_number_digits = 26 ** num_digits
        while largest_number_digits < largest_number:
            if column_number > largest_number_digits:
                num_digits += 1
                largest_number_digits = 26 ** num_digits + largest_number_digits
            else:
                break

        print("num_digits: ", num_digits)

        column_str = ""
        power = num_digits - 1
        while power >= 0:
            i = 26
            while i > 0:
                # print("compare value ", i, i * (26 ** power), column_number)
                if i * (26 ** power) > column_number:
                    i -= 1
                else:
                    break
            column_str += chr(64 + i)
            column_number -= i * (26 ** power)
            power -= 1

        return column_str


ans = Solution.convert_to_title(1)
print("ans is ", ans)

ans = Solution.convert_to_title(28)
print("ans is ", ans)

ans = Solution.convert_to_title(701)
print("ans is ", ans)

ans = Solution.convert_to_title(731)
print("ans is ", ans)

ans = Solution2.convert_to_title(1)
print("ans is ", ans)

ans = Solution2.convert_to_title(28)
print("ans is ", ans)

ans = Solution2.convert_to_title(701)
print("ans is ", ans)

ans = Solution2.convert_to_title(731)
print("ans is ", ans)
