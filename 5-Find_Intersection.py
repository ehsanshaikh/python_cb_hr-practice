# Find Intersection
# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
import string

def FindIntersection(strArr):
    lst1 = []
    lst2 = []
    res = ""
    for i in range(len(strArr)):
        lst = strArr[i].translate(str.maketrans('', '', string.punctuation))
        if i==0:
            lst1 = list(map(int, lst.split(" ")))
        if i==1:
            lst2 = list(map(int, lst.split(" ")))
    for i in lst1:
        if i in lst2:
            res += str(i)+","
    result = res.rstrip(res[-1])
    return result

print(FindIntersection(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]))