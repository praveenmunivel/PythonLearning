
# Problem 3 : identify pairs of strings that when concatenated contain all 26 alphabets
# It involves iterating over 2 sets of string

def is_matching(str1: str, str2: str):
    combined_str = (str1+str2).lower()
    print(combined_str)
    return set("abcdefghijklmnopqrstuvwxyz").difference(set(combined_str))

print(is_matching("the quick brown fox", "jumps over a lazy dog %%"))