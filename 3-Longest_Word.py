# Longest Word
# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
import string

def LongestWord(sen):
    new_string = sen.translate(str.maketrans('', '', string.punctuation))
    set1 = new_string.split(' ')
    max_len = -1
    result = ""
    for s in set1:
        if len(s)>max_len:
            max_len = len(s)
            result = s
            # code goes here
    return result

# keep this function call here
print(LongestWord(input()))