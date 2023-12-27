numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(num):
    return num % 2 == 0

even = filter(is_even, numbers)
print(list(even))
print(list(even), "haha")


a = [1, 2, 3, 4, 5, 6]
b = [1, 4, 5, 6]
c = [4, 6, 1]

print((set(a).intersection(b)).intersection(c))

print(bool(''))


from functools import reduce

def count_words(doc):
    normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for i in normalised_doc.split():
        frequencies[i] = frequencies.get(i, 0) + 1
    return frequencies

documents = [
    'It was the best of times, it was the worst of times.',
    'I went to the woods because I wished to live deliberately, to front only the essential facts of life',
    'Friends, Rromans, countrymen, lend me your ears; I come to bury Caesar, not praise him',
    'I do not like green eggs and ham. I do not like them, Sam-I-Am',
]

counts = map(count_words, documents)
# we exhausted the map, so the next time we use counts, we will get nothing.
# That is why reduce will throw an error.
# print(list(counts)) 

def combine_counts(doc1, doc2):
    combined_doc = doc1.copy()
    for k, v in doc2.items():
        combined_doc[k] = combined_doc.get(k, 0) + v
    return combined_doc

print(reduce(combine_counts, counts))