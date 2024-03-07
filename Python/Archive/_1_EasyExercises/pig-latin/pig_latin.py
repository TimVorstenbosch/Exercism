VOWELS = ("a", "e", "i", "o", "u")

def find_index_of_vowel_in_string(text: str) -> int:
    for idx, character in enumerate( list(text) ):
        if character in VOWELS:
            return idx
    return 0 # in case there is no vowel in the word, you don't have to move any part of the string

def translate(text: str) -> str:

    splitted_text = text.lower().split(" ")
    new_text = []

    for text_part in splitted_text:

        y_idx = text_part.find("y")

        # x & y are checked here for vowel sounds 
        #   -> assumption that if a word starts with x or y, it is a vowel if the next letter is not a vowel
        if text_part.startswith( VOWELS ) or ( text_part.startswith(("x", "y")) and text_part[1] not in VOWELS ):
            new_text.append( text_part + "ay" )
        
        elif text_part.startswith("qu"):
            new_text.append( text_part[2:] + "quay" )
        
        elif text_part[1:].startswith("qu"):
            new_text.append( text_part[3:] + text_part[0] + "quay" )

        # y_idx = -1 -> "y" needs to be found in the text part
        elif y_idx != -1 and text_part[0] != "y" and not any( vowel in text_part[:y_idx] for vowel in VOWELS ):
            new_text.append( text_part[y_idx:] + text_part[:y_idx] + "ay" )

        else:
            vowel_idx = find_index_of_vowel_in_string(text_part)
            new_text.append( text_part[vowel_idx:] + text_part[:vowel_idx] + "ay" )
    
    return " ".join(new_text)
