# Questions Marks
# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.
# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
def QuestionsMarks(strParam):
    a = -1
    b = -1
    c = 0
    count = 0
    lst = list(strParam)
    while count != len(lst):
        for i in lst:
            count = count + 1
            if i.isnumeric() and c==1:
                c = c + 1
                b = lst.index(i)
            if i.isnumeric() and c==0:
                c = c + 1
                a = lst.index(i)
            if c==2 and (int(lst[a])+int(lst[b]))==10:
                c=0
                d = a + 1
                lst1 = lst[d:b]
                charCount = 0
                for s in lst1:
                    charCount += s.count("?")
                    if charCount == 3:
                        return "true"
    return "false"

print(QuestionsMarks(input()))