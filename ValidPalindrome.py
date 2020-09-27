# -*- coding: utf-8 -*-
# Given a string, determine if that string is a palindrome after at most one character deletion.
# for example, Input: “dad” -> Output: True, Input: “dade” -> Output: False ....Explanation: You can delete the character “e”
# A palindrome is a phrase which reads the same backward as forward (In japanese, '回文')

def checkPalindrome(string):
    left = 0
    right = len(string)-1
    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

s = "dad"
print(checkPalindrome(s))
s = "dade"
print(checkPalindrome(s))
s = "dd"
print(checkPalindrome(s))

