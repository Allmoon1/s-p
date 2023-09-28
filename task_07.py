def combine_anagrams(array):
    anagrams = []

    if not array:
        return anagrams
 
    sorted_elem_lst = [''.join(sorted(word)) for word in array]
 
    d = {}
    for k, v in enumerate(sorted_elem_lst):
        d.setdefault(v, []).append(k)

    for index in d.values():
        collection = []
        for i in index:
            collection.append(array[i])
        if len(collection) >= 1:
            anagrams.append(collection)
 
    return anagrams

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))