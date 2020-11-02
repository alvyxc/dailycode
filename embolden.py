#Implement the function embolden(s, lst) which takes in a string s and list of substrings lst,
# and wraps all substrings in s with an HTML bold tag <b> and </b>.

#If two bold tags overlap or are contiguous, they should be merged.

#For example, given s = abcdefg and lst = ["bc", "ef"], return the string a<b>bc</b>d<b>ef</b>g.

#Given s = abcdefg and lst = ["bcd", "def"], return the string a<b>bcdef</b>g, since they overlap.


def merge (s1, s2):

    i = 0
    for c in s1:
        if c == s2[0]:
            break
        i = i + 1

    return s1[0:i] + s2

def unmerge (s1, s2):

    i = 0
    for c in s1:
        if c == s2[0]:
            break
        i = i + 1

    return s1[0:i]


def embolden(s, lst, currentList):

    combine_str = s
    if currentList:
        combine_str = currentList[len(currentList)-1][1] + s

    for l in lst:
        if l in s:
            currentList.append((0, unmerge(s, l)))
            currentList.append((1, l))
            lst.remove(l)
            return ""
        if l in combine_str:
            currentList[len(currentList) - 1] = (1, merge(currentList[len(currentList) - 1][1], l))
            lst.remove(l)
            return ""

    return s


# main

#s = "abcdefg"
#lst = ["bc", "ef"]
s = "abcdefg"
lst = ["bcd", "def"]

total_list = []
current_s = ""

for c in s:
    current_s = current_s + c
    current_s = embolden(current_s, lst, total_list)

if current_s != "":
    total_list.append((0, current_s))

print(total_list)