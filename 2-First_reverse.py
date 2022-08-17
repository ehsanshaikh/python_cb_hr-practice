# First Reverse
# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

def FirstReverse(strParam):
    new_str = ""
    new_str_len = len(strParam)
    for i in range(len(strParam)):
        if strParam[new_str_len-1] is not None:
            new_str = new_str + strParam[new_str_len-1]
        else:
            new_str = " " + strParam[new_str_len-1]
        new_str_len = new_str_len - 1
    return new_str

# keep this function call here
print(FirstReverse(input()))