import itertools

LIST_OF_POSSIBLE_NUMBERS= [1,2,3,4,5,6,7,8,9]

def combinations(target: int, size: int, exclude: list) -> list:

    list_of_numbers_to_check = [number for number in LIST_OF_POSSIBLE_NUMBERS if number not in exclude]
    print(list_of_numbers_to_check)
    list_of_combinations = []

    if size == 1 and target > 9:
        return [[]]

    elif size == 1:
        return [[target]]
    
    else:
        for comb in itertools.combinations(list_of_numbers_to_check, size):
            if sum(comb) == target:
                list_of_combinations.append( sorted(list(comb)) )

    return list_of_combinations
            

# print( combinations( 10, 2, [1,4]) )
