from collections import Counter
import string

def count_words(input_string):
    cleaned_string = input_string.translate(str.maketrans("", "", string.punctuation)).lower()
    word_count = Counter(cleaned_string.split())
    
    return dict(word_count)

print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}
