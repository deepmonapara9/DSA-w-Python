from math import *

# This will reverse the number like last to front and using floor divison
# Output: 3785
n = 5873
n = 121
num = n

# Space Complexity: O(1)
# This will reverse the number like last to front and using floor divison
# Output: 3785
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10

# count the number
count = 0
while num > 0:
    count += 1
    num = num // 10
print(count)

# using logarithm
def count_digits(num):
   return int(log10(num)) + 1


# Check palindrome
# Time Complexity: o(log10(N))
# Space Complexity: O(1)
# result = 0
# while num > 0:
#    ld = num % 10 # 3
#    result = result * 10 + ld # 0 * 10 + 3
#    num = num // 10
# if result == n:
#    print("palindrome")
# else:
#    print("not palindrome")

# Leetcode 9 solution for palindrome number
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = x
        palindrome_number = 0
        while num > 0:
            last_digit = num % 10
            palindrome_number = (palindrome_number * 10) + last_digit
            num //= 10
        return palindrome_number == x


# Armstrong number
# Time Complexity: o(log10(N) * d) where d is number of digits
# Space Complexity: O(1)
n = 153
num = n
nod = len(str(n))
total = 0

while num > 0:
   ld = num % 10
   total = total + (ld ** nod)
   num = num // 10
if total == n:
   print("Armstrong")   
else:
   print("Not Armstrong")