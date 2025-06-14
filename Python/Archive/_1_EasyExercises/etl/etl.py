def transform(legacy_data):
    return {letter.lower():point for point,letter_list in legacy_data.items() for letter in letter_list}