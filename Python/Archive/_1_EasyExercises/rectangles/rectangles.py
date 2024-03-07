
from collections import namedtuple
from itertools import product

Location = namedtuple("Location", "row col")

def determine_corners_and_incorrect_locations(matrix: str) -> tuple[list, list]:
    corner_list = []
    incorrect_locations = []
    corner_columns = []

    for r_idx, row in enumerate(matrix):
        corner_in_row = False

        for c_idx, character in enumerate(row):

            new_location = Location(r_idx, c_idx)

            if character == "+":
                corner_in_row = True
                corner_columns.append(c_idx)
                corner_list.append( new_location ) 

            # The first check is to ensure only symbols between corners are checked (sides), to improve efficiency in the next phase
            # The last check is to avoid "-" in vertical sides and "|" in horizontal sides
            elif character not in ["|", "-"] and (corner_in_row or c_idx in corner_columns) \
            or ( (character == '-' and corner_in_row == False) or (character == '|' and c_idx not in corner_columns ) ):
                incorrect_locations.append( new_location )

    return (corner_list,  incorrect_locations)


def check_sides_rectangle_are_correct(tl_corner:tuple, tr_corner:tuple, bl_corner:tuple, br_corner:tuple, incorrect_locs: list) -> bool:
    
    #check top side first ,then left, right and finally bottom side
    for row, col in incorrect_locs:
        if (tl_corner.row == row and tl_corner.col < col < tr_corner.col) \
        or (tl_corner.col == col and tl_corner.row < row < bl_corner.row) \
        or (tr_corner.col == col and tr_corner.row < row < br_corner.row) \
        or (bl_corner.row == row and bl_corner.col < col < br_corner.col):
            return False
        
    return True


def count_rectangles(corners: list, incorrect_locs:list) -> int:

    count = 0

    for top_left_corner in corners: 

        # only check corners to the right or bottom of the current corner, skips backwards rectangles
        possible_hor_corners = [corner for corner in corners if corner.row == top_left_corner.row and corner.col > top_left_corner.col ]
        possible_ver_corners = [corner for corner in corners if corner.col == top_left_corner.col and corner.row > top_left_corner.row]

        corner_combinations = product(possible_hor_corners, possible_ver_corners)

        for hor_corner, ver_corner in corner_combinations:
            bottom_right_corner = Location(ver_corner.row, hor_corner.col)

            if bottom_right_corner in corners:
                all_sides_correct = check_sides_rectangle_are_correct(top_left_corner, hor_corner, ver_corner, bottom_right_corner, incorrect_locs)

                if all_sides_correct:
                    count+=1

    return count


def rectangles(strings: list) -> int:

    matrix = [[*string] for string in strings] 
    corner_list, incorrect_locations = determine_corners_and_incorrect_locations(matrix)
    number_of_rectangles = count_rectangles(corner_list, incorrect_locations)

    return number_of_rectangles

