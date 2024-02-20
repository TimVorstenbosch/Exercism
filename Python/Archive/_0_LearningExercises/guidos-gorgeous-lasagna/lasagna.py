"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
TIME_PER_LAYER = 2


def bake_time_remaining(time_in_oven):
    """
    Calculate the time remaining for baking the lasagna

    :param time_in_oven: int - time the lasagna was in the oven
    :return: int - time remaining for the lasagna

    This function takes an integer representing the time the lasagna was in the oven
    and returns the time the lasagna needs to remain in the oven.
    """
    return EXPECTED_BAKE_TIME - time_in_oven


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time given the number of layers.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes an integer representing the number of lasagna layers and 
    multiplies them with the constant TIME_PER_LAYER
    """
    return TIME_PER_LAYER * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time



