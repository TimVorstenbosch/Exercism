from collections import Counter

def is_isogram(string):
    replaced_str = string.replace(" ", "").replace("-", "").lower()
    return len(set(replaced_str)) == len(replaced_str)
    #sum( [ cnt for cnt in Counter( [*replaced_str] ).values() if cnt == 1 ] ) == len(replaced_str)
