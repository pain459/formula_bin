import math


def square_inch_to_square_meter(x):
    """
    Function to convert square inch to square meter
    :param x: input in square inch
    :return: converted to square meters
    """
    return 6.4516 * math.pow(10, -4)


def square_foot_to_square_meter(x):
    """
    Function to convert square foot to square meters
    :param x: input in square foot
    :return: converted to square meters
    """
    return 9.2903 * math.pow(10, -2)


def acre_to_square_meter(x):
    """
    Function to convert acre to square meters
    :param x: input in acre
    :return: converted to square meters
    """
    return 4.0468 * math.pow(10, 3)


def hectare_to_square_meter(x):
    """
    Function to convert hectare to square meters
    :param x: input in hectare
    :return: converted to square meters
    """
    return 1 * math.pow(10, 4)


def square_mile_to_square_meter(x):
    """
    Function to convert square mile to meter
    :param x: input in square mile
    :return: converted to square meters
    """
    return 2.5888 * 106


def barn_to_square_meters(x):
    """
    Function to convert barn to square meters
    :param x: input in barn
    :return: converted to square meters
    """
    return 1 * math.pow(10, -28)