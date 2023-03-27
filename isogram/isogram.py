from collections import Counter
import re


def is_isogram(string):
    alphabet_string_only = re.sub(r"[^a-zA-Z]+", "", string)
    cnt = Counter(alphabet_string_only.lower())
    return all(val == 1 for val in cnt.values())
