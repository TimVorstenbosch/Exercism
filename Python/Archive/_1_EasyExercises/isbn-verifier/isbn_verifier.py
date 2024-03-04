import re

def is_valid(isbn):

    check_isbn = isbn.replace("-", "")
    
    # _ = dummy in case of empty string, 9 = dummy variable to allow the X at the end for the regex search
    regex_search = re.search("[A-z]", check_isbn if ("_" + check_isbn)[-1] != "X" else check_isbn[:-1] + "9") 

    if len(check_isbn) != 10 or regex_search != None: #not None, so a letter is found
        return False    
    else:
        return sum( [int(value) * (10-idx) if value != "X" else 10 * (10-idx) for idx, value in enumerate( list( check_isbn ) ) ] ) % 11 == 0
