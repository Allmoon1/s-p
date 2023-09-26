def isAnagram(string1, string2):
    if len(string1) != len(string2):
        return False
    dict_str1 = {}
    dict_str2 = {}
    for i in range(len(string1)):
        dict_str1[string1[i]] = dict_str1.get(string1[i], 0) + 1
    for i in range(len(string2)):
        dict_str2[string2[i]] = dict_str2.get(string2[i], 0) + 1
    return dict_str1 == dict_str2


def combine_anagrams(array):
    if len(array) < 2:
        raise ValueError("WrongInputError")

    for elem in array: elem = elem.lower()
    anagrams_combime = dict.fromkeys([array], set())
    print(anagrams_combime)
    for i in range(0, len(array)):
        anagrams_combine.append([array[i]])
        for j in range(0, len(array)):
            if isAnagram(array[i], array[j]):
                anagrams_combine[i].append(array[j])

    
    return anagrams_combine

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))