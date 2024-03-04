
def is_pangram(sentence):
    return len( set( [x.lower() for x in [*sentence] if str.isalpha(x) ] ) ) == 26
