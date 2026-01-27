"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
LAYER_PREP_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(number_of_layers):
    """
    Calcualtes the preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :global constant LAYER_PREP_TIME: int - the time taken to prepare one layer
    :return: int - total time of preparation

    This function takes two integers representing the number of layers in the lasagna and the time it takes to prepare a single layer and returns the total prepariton time.
    """
    return LAYER_PREP_TIME * number_of_layers
    


def elapsed_time_in_minutes(number_of_layers, elasped_bake_time):
    """
    Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layersm, calculates the preparation time and the total elapsed minutes spent cooking the lasagna and returns the total time.
    """
    return preparation_time_in_minutes(number_of_layers) + elasped_bake_time



