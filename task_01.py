def is_palindrome(string):
    reworked_string = ''.join(char for char in str(string) if char.isalnum()).lower()
    return reworked_string == reworked_string[::-1]

#print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
#print(is_palindrome("Madam, I'm Adam!")) # => True
#print(is_palindrome(333)) # => True
#print(is_palindrome(None)) # => False
#print(is_palindrome("Abracadabra")) # => False