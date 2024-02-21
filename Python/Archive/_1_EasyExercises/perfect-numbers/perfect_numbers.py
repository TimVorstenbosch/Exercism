import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1 : 
        raise ValueError("Classification is only possible for positive integers.")
    
    aliquot_sum = 0 if number == 1 else CalculateAliquotSum(number)

    if number == aliquot_sum : return "perfect"
    elif number < aliquot_sum : return "abundant"
    else : return "deficient" 


def CalculateAliquotSum(number):
    return sum( [i for i in range( 1, math.ceil(number/2 + 1) ) if number % i == 0 ] )
