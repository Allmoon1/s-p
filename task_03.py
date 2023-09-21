def max_odd(array):
    max = 0
    for elem in array:
        if (type(elem) == int) or (type(elem) == float):
            if (int(elem) % 2 == 1) and (elem > max):
                max = int(elem)
    if max != 0:
        return max
    else:
        return None

print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4])) # => None)