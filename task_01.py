def is_palindrome(string):
    s = ''.join(c for c in str(string) if c.isalnum()).lower()
    return s == s[::-1]


print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra")) # => False