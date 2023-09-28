import re

def multiply_numbers(inputs = None):
    inputs = str(inputs)
    digits = list(map(str,re.findall('(\d+)|[+-]?[0-9]+\.[0-9]+', inputs)))
    if (inputs == "None") or (len(digits) == 0):
        return None
    result = 1
    for digit in digits:
        for char in digit:
            result = int(char)*result

    return result


print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120