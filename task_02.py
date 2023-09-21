#class range(object):
#    def __init__(self, a, b):
#        self.coord = (a, b)

def coincidence(list = [], range = None):
     result = []
     if (len(list) == 0) or (range is None):
         return result
     else:
         for element in list:
             if (type(element) == int) or (type(element) == float):
                 if (element >= range[0]) and (element <= range[-1]):
                     result.append(element)
     return result
     

print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
print(coincidence()) # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]
