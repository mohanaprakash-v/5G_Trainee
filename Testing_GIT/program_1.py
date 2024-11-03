# Function which return reverse of a string - To check wheteher a string is palindrome or not

def isPalindrome(string):
    return s == s[::-1]


string = "malayalam"
result = isPalindrome(string)

if result:
    print("Yes")
else:
    print("No")
