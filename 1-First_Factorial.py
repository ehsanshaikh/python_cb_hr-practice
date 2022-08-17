# First Factorial
# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.

def FirstFactorial(num):
    dum = num
    dum1 = num
    while True:
        dum1 = dum1-1
        if dum1==0:
            return dum
        dum = (dum*(dum1))

print(FirstFactorial(int(input())))