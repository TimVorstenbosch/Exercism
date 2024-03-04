def rotate(text, key) -> str:
    rotated_text = ""

    for character in [*text]:
        if not character.isalpha():
            rotated_text += character
        elif character.isupper():
            rotated_text += chr( ord("A") + ( (ord(character) - ord("A") + key) % 26) )
        else: 
            rotated_text += chr( ord("a") + ( (ord(character) - ord("a") + key) % 26) )

    return rotated_text
