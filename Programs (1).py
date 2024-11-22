#Python program to delete duplicates from list

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
out=[]
for i in test_list:
    if i not in out:
        out.append(i)
print(out)

#using built in functions

print(list(set(test_list)))


#Python | Remove all duplicates words from a given sentence


s = "Python is great and Java is also great"

l=s.split()

k=[]

for i in l:
    if (s.count(i)>=1 and (i not in k)):
        k.append(i)
print(' '.join(k))


string = 'Python is great and Java is also great'

print(' '.join(dict.fromkeys(string.split())))
'''

#Python | Largest, Smallest, Second Largest, Second Smallest in a List
'''
inp=[22, 85, 62, 40, 55, 12, 39, 2, 43]

inp.sort()
print("smallest element is :",inp[0])
print("second smallest element is :",inp[1])
print("largest element is :",inp[-1])
print("second largest element is :",inp[-2])
'''
#Find smallest element in list
'''
list1 = [10, 20, 4, 45, 99]

k=list1[0]

n=len(list1)
for i in range(0,n):
    if list1[i]<k:
        k=list1[i]
print(k)
'''

#Find largest element in list
'''
list1 = [10, 20, 4, 45, 99]

k=list1[0]

n=len(list1)
for i in range(0,n):
    if list1[i]>k:
        k=list1[i]
list1.remove(k)
print(list1)
m=list1[0]

n=len(list1)
for i in range(len(list1)):
    if list1[i]>m:
        m=list1[i]
print(m)
'''
#Python program to find N largest elements from a list
'''
n=3
inp=[81, 52, 45, 10, 3, 2, 96]

inp.sort()
print(inp[-n:])

emp=[]
for i in range(0,n):
    k=inp[0]
    for i in range(len(inp)):
        if inp[i]>k:
            k=inp[i]
    inp.remove(k)
    emp.append(k)
print(emp)
'''
# Python program to print Even Numbers in a List
'''
list1 = [10, 21, 4, 45, 66, 93]
for i in list1:
    if i%2==0:
        print(i,end=" ")
'''
#Python | Remove empty tuples from a list
'''
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
tuples = filter(None, tuples)
print(tuples)

'''

##Python | To add two numbers
'''
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
sum=num1+num2
print("sum of {0} and {1} is {2}".format(num1,num2,sum))
'''
# Program to generate a random number between 0 and 9

# importing the random module
'''
import random

print(random.randint(0,9))
'''
#Python Program to Check Leap Year
'''
i=int(input("enter the year:"))
if i%4==0:
    if (i%100==0):
        if i%400==0:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
else:
    print("No")
'''
#Python Program to Find the Largest Among Three Numbers
'''
num1 = 10
num2 = 14
num3 = 12
if (num1>=num2) and (num1>=num3):
    largest=num1
elif (num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3
print(largest)
'''
#Python Program to Print all Prime Numbers in an Interval
'''
m=900
n=1000
for i in range(m,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
'''
# Python program to find the factorial of a number provided by the user.
'''
# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
Output

The factorial of 7 is 5040
'''
#Python Program to Display the multiplication Table
'''
n=int(input("enter the number:"))

for i in range(1,11):
      print(n ,'x',i,'=',n*i)
'''
#Python Program to Print the Fibonacci sequence
'''
n=10

n1,n2=0,1
while n > 0:
    print (n1)
    nth=n1+n2
    n1=n2
    n2=nth
    n-=1
'''
# Python program to check if the number is an Armstrong number or not
#153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
# take input from the user
'''
num = int(input("Enter a number: "))
temp=num
i=0
while temp>0:
    a=temp%10
    i=i+a**3
    temp//=10
# display the result
if num == i:
   print(num,"is an Armstrong number")
else:
   print(num,"is not a Armstrong number")
'''

#Python Program to Find the Sum of Natural Numbers
'''
num=16
sum=0
while num>0:
    sum+=num
    num-=1
print(sum)
'''
#Reverse string in Python (5 different ways)
'''
list1="vamsi"
s=""
for i in list1:
    s=i+s
    print(s)
print(s)

o/p:

v
av
mav
smav
ismav
ismav


s="vamsi"
s1=s[::-1]
print(s1)
'''
# Python program to remove all special characters from string
'''
# importing RegEx module
import re

# take string
string = input('Enter any string: ')
 
# using regular expression to remove special characters
new_string = re.sub(r'[^a-zA-Z0-9]','',string)

# print string without special characters
print('New string:', new_string)
'''
#Python Program to Remove Duplicates From List

'''
inp=[1,2,3,4,5,1,2,3,4]
k=[]

for i in inp:
    if i not in k:
        k.append(i)
print(k)

#Python Program for string comprehession
"""

Input: aabbccaabb
output: a2b2c2a2b2

 

s="aaaaabbccaabb"
i=0
n=len(s)

while i < n-1:
    count=1
    while (i < n-1 ) and s[i]==s[i+1]:
        count+=1
        i+=1
        
    i+=1

    print(s[i-1]+str(count),end="")
"""
#Python program to reverse a sentense

inp="This is a new year"
a=inp.split(" ")
print (a)
n=len(a)
print (n)
out=[]

print(a[n-1])

while n > 0:
    out.append(a[n-1])
    n-=1
print(" ".join(out))

"""  

#Python program to push zeros to end in a list
#[1,2,0,9,0,8,6,5,4,0,1]
"""
inp=[1,2,0,9,0,8,6,5,4,0,1]

out=[]

n=len(inp)

print (n)
count=0
for i in range(0,n):
    if inp[i] != 0:
        out.append(inp[i])
        count+=1

while count < n:
    out.append(0)
    count+=1
print(out)

"""


"""
employee_info = {"Raju": {"HW": "Laptop", "Config":{"RAM": 16, "CPU": 8}},
                 "Ramu": {"HW": "Laptop", "Config":{"RAM": 12, "CPU": 8}},
                 "Gopi": {"HW": "Laptop", "Config":{"RAM": 8, "CPU": 8}} }

#print(employee_info['Raju']['Config']['RAM'])

for key,value in employee_info.items():
    print (key,employee_info[key]['Config']['RAM'])

"""

#Python program to print snake pattern

"""
#[[1,2,3],[4,5,6],[7,8,9]]

#123654789
inp=[[1,2,3],[4,5,6],[7,8,9]]

n=len(inp)
#print (n)

for i in range (0,n):
    if i % 2==0:
        #print("inside if")
        for j in range (0,n):
            print(inp[i][j],end="")
    else:
        for j in range (n-1,-1,-1):
            print(inp[i][j],end="")
"""           

#Balanced String
"""
str = "{}(){]{]]"
c=0
for i in str:
    print(i)
    if i == "{" or i == "(" or i == "[":
        c+=1
    elif i == "}" or i == ")" or i == "]":
        c-=1
if c == 0:

##suffixprefix
def largest_contiguous_prefix_suffix(str1, str2):
    n = min(len(str1), len(str2))
    prefix = ""
    suffix = ""

    for i in range(n):
        if str1[:i+1] == str2[:i+1]:  # Check for prefix
            prefix = str1[:i+1]
        else:
            break

    for i in range(n):
        if str1[-i-1:] == str2[-i-1:]:  # Check for suffix
            suffix = str1[-i-1:]
        else:
            break

    return prefix, suffix

# Example usage:
str1 = "abcdef"
str2 = "abcfef"
prefix, suffix = largest_contiguous_prefix_suffix(str1, str2)
print("Largest contiguous prefix:", prefix)
print("Largest contiguous suffix:", suffix)

    print ("balanced")
else:
    print("unbalaced")
""" 
###adding complex numbers
def add_complex(a, b):
    # Parse real and imaginary parts of both complex numbers
    a_real, a_imaginary = map(int, a[:-1].split('+'))
    b_real, b_imaginary = map(int, b[:-1].split('+'))

    # Add real and imaginary parts separately
    real_part = a_real + b_real
    imaginary_part = a_imaginary + b_imaginary

    # Construct the result string
    return str(real_part) + '+' + str(imaginary_part) + 'i'

# Example usage
result = add_complex("1+2i", "2+3i")
print("Result:", result)


##Longest Substring Without Repeating Characters

Answer:
def longest_substring_with_length_and_string(s: str) -> (int, str):
    last_seen = {}
    start = 0
    max_length = 0
    longest_substring = ""
    
    for i, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        
        last_seen[char] = i
        current_length = i - start + 1
        if current_length > max_length:
            max_length = current_length
            longest_substring = s[start:i+1]
    
    return max_length, longest_substring

# Test cases
print(longest_substring_with_length_and_string("abcabcbb"))  # Output: (3, 'abc')
print(longest_substring_with_length_and_string("bbbbb"))     # Output: (1, 'b')
print(longest_substring_with_length_and_string("pwwkew"))    # Output: (3, 'wke')


###Python function to find the longest palindromic substring in a given string:####
def longest_palindromic_substring(s: str) -> str:
    if len(s) <= 1:
        return s
    
    longest = ""
    
    for i in range(len(s)):
        # Check odd-length palindromes
        odd_palindrome = expand_around_center(s, i, i)
        # Check even-length palindromes
        even_palindrome = expand_around_center(s, i, i+1)
        
        # Update longest palindrome found so far
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest

def expand_around_center(s: str, left: int, right: int) -> str:
    # Expand around center and check if the substring is palindrome
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Return the palindrome substring
    return s[left+1:right]

# Test cases
print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"
print(longest_palindromic_substring("cbbd"))   # Output: "bb"
print(longest_palindromic_substring("a"))      # Output: "a"

#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # Create an array of empty strings, each string represents a row
    rows = [''] * numRows
    # Initial position for traversing the string
    current_row = 0
    direction = 1  # 1 for downward, -1 for upward

    for char in s:
        rows[current_row] += char  # Add current character to the corresponding row
        # Change direction if at the top or bottom row
        if current_row == 0:
            direction = 1
        elif current_row == numRows - 1:
            direction = -1
        # Move to the next row
        current_row += direction

    # Concatenate all rows to form the zigzag pattern
    result = ''.join(rows)
    return result

# Test case
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"

###generate paranthesis#####
def generate_parenthesis(n):
  """
  :type n: int
  :rtype: List[str]
  """
  res = []

  def backtrack(s, left, right):
    if len(s) == 2 * n:
      res.append(s)
      return
    if left < n:
      backtrack(s + '(', left + 1, right)
    if right < left:
      backtrack(s + ')', left, right + 1)

  backtrack("", 0, 0)
  return res

# Test cases
print(generate_parenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
print(generate_parenthesis(1))  # Output: ["()"]

#####Given two strings needle and aystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
def strStr(haystack, needle):
  """
  :type haystack: str
  :type needle: str
  :rtype: int
  """
  # Check for empty needle or haystack being larger than needle
  if not needle or len(haystack) < len(needle):
    return -1

  # Iterate through haystack
  for i in range(len(haystack) - len(needle) + 1):
    # Check if current substring matches the needle
    if haystack[i:i + len(needle)] == needle:
      return i

  # No match found
  return -1

# Test cases
print(strStr("sadbutsad", "sad"))  # Output: 0
print(strStr("leetcode", "leeto"))  # Output: -1
####Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.####

def letterCombinations(digits: str):
    if not digits:
        return []
    
    # Create a mapping from each digit to the letters it represents
    digit_map = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Function to generate letter combinations
    def backtrack(index, path):
        # If the current combination is of the same length as the digits string, add it to the result
        if len(path) == len(digits):
            combinations.append(''.join(path))
            return
        
        # Get the letters corresponding to the current digit
        letters = digit_map[digits[index]]
        # Explore each letter and backtrack
        for letter in letters:
            path.append(letter)  # Add the current letter to the path
            backtrack(index + 1, path)  # Move to the next digit
            path.pop()  # Remove the last letter to backtrack
            
    combinations = []
    backtrack(0, [])  # Start backtracking from the first digit
    return combinations

# Test cases
print(letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations(""))    # Output: []
print(letterCombinations("2"))   # Output: ["a","b","c"]


###You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 ####
 from collections import defaultdict

def findSubstring(s, words):
  """
  :type s: str
  :type words: List[str]
  :rtype: List[int]
  """
  if not words or not words[0]:
    return []

  word_len = len(words[0])
  total_len = word_len * len(words)
  word_count = defaultdict(int)
  for word in words:
    word_count[word] += 1

  res = []
  for i in range(len(s) - total_len + 1):
    current_count = defaultdict(int)
    for j in range(i, i + total_len, word_len):
      current_word = s[j:j + word_len]
      if current_word not in word_count or current_count[current_word] >= word_count[current_word]:
        break
      current_count[current_word] += 1
    else:
      res.append(i)

  return res

# Test case
print(findSubstring("barfoothefoobarman", ["foo","bar"]))  # Output: [0,9]

def findSubstring(s: str, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    concat_len = word_len * num_words
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    result_indices = []

    for i in range(len(s) - concat_len + 1):
        seen_words = {}
        j = 0
        while j < num_words:
            word_index = i + j * word_len
            word = s[word_index:word_index + word_len]
            if word not in word_count:
                break
            seen_words[word] = seen_words.get(word, 0) + 1
            if seen_words[word] > word_count[word]:
                break
            j += 1
        if j == num_words:
            result_indices.append(i)

    return result_indices

# Test cases
print(findSubstring("barfoothefoobarman", ["foo","bar"]))  # Output: [0,9]
print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))  # Output: []
print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))  # Output: [6,9,12]


####To solve the "count-and-say" problem, we need to generate the sequence iteratively up to the nnn-th term. Each term in the sequence is derived from the previous term by describing the frequency and value of consecutive digits.
def countAndSay(n: int) -> str:
    def next_number(s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            count = 1  # We have seen at least one occurrence of s[i]
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)
    
    current = "1"
    for _ in range(n - 1):
        current = next_number(current)
    return current

# Test case
print(countAndSay(4))  # Output: "1211"
###Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

def multiply(num1, num2):
  """
  :type num1: str
  :type num2: str
  :rtype: str
  """
  # Handle empty cases
  if not num1 or not num2:
    return "0"

  # Reverse the strings for easier digit-by-digit multiplication
  num1 = num1[::-1]
  num2 = num2[::-1]

  result = 0
  for i, digit1 in enumerate(num1):
    carry = 0
    for j, digit2 in enumerate(num2):
      # Digit-by-digit multiplication with carry
      product = int(digit1) * int(digit2) + carry
      carry, digit = divmod(product, 10)
      # Add the partial product to the result at the appropriate position
      result += digit * 10**(i + j)
    # Add remaining carry from the last multiplication in the current digit1 loop
    result += carry * 10**(i + j + 1)

  # Convert the final result back to a string
  return str(result)

# Test cases
print(multiply("2", "3"))  # Output: "6"
print(multiply("123", "456"))  # Output: "56088"

####Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0


def firstUniqChar(s: str) -> int:
    # Step 1: Build the frequency count
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    
    # Step 2: Find the first non-repeating character
    for index, char in enumerate(s):
        if frequency[char] == 1:
            return index
    
    return -1

# Test cases
print(firstUniqChar("leetcode"))  # Output: 0
print(firstUniqChar("loveleetcode"))  # Output: 2
print(firstUniqChar("aabb"))  # Output: -1

###Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
 def reverseVowels(s):
  """
  :type s: str
  :rtype: str
  """
  vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
  s = list(s)  # Convert string to list for in-place modification
  left, right = 0, len(s) - 1
  while left < right:
    while left < right and s[left] not in vowels:
      left += 1
    while left < right and s[right] not in vowels:
      right -= 1
    if left < right:
      s[left], s[right] = s[right], s[left]
      left += 1
      right -= 1
  return ''.join(s)

# Test cases
print(reverseVowels("hello"))  # Output: "holle"
print(reverseVowels("leetcode"))  # Output: "leotcede"


####mergetwostrings
def mergeStrings(word1, word2):
  """
  :type word1: str
  :type word2: str
  :rtype: str
  """
  res = ""
  # Iterate through characters of both strings simultaneously using min length
  for i in range(min(len(word1), len(word2))):
    res += word1[i]
    res += word2[i]

  # Append remaining characters from longer string
  res += word1[i+1:] if len(word1) > len(word2) else word2[i+1:]
  return res

# Test cases
print(mergeStrings("abc", "pqr"))  # Output: "apbqcr"
print(mergeStrings("a", "b"))  # Output: "ab"

#write a function to return monotically increasing odd number till the given seed value


def print_increasing_odd_numbers(seed):
    if seed < 0:
        for i in range(a, 0):
            if i % 2 != 0:
                print(i)
    else:
        for i in range(seed + 1):
            if i % 2 != 0:
                print(i)

# Input from the user
a = int(input("Enter the seed value: "))
print_increasing_odd_numbers(a)