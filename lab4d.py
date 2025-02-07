#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    return string[:5]
    # Place code here - refer to function specifics in section below

def last_seven(string):
    return string[-7:]
    # Place code here - refer to function specifics in section below

def middle_number(num):
    numstr = str(num)
    return numstr[1:3]
    # Place code here - refer to function specifics in section below

def first_three_last_three(arg1, arg2):
    return arg1[:3] + arg2[-3:]
    # Place code here - refer to function specifics in section below


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))