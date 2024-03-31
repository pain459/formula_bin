import math


def inch_to_centimeter(x):
    """
    Function to convert from inch to centimeter
    :param x: input in inches
    :return: converted to centimeters
    """
    return x * 2.540


def centimeter_to_inch(x):
    """
    Function to convert from centimeter to inch
    :param x: input in centimeters
    :return: converted to inches
    """
    return x / 2.540


def millimeter_to_meter(x):
    """
    function to convert from millimeter to meter
    :param x: input in millimeters
    :return: converted to meters
    """
    return x * 0.001


def centimeter_to_meter(x):
    """
    Function to convert from centimeter to meter
    :param x: input in centimeter
    :return: converted to meters
    """
    return x * 0.01


def decimeter_to_meter(x):
    """
    Function to covert from decimeter to meter
    :param x: input in decimeter
    :return: converted to meters
    """
    return x * 0.1


def decameter_to_meter(x):
    """
    Function to convert decameter to meter
    :param x: input in decameter
    :return: converted to meters
    """
    return x * 10


def hectometer_to_meter(x):
    """
    Function to convert hectometer to meter
    :param x: input in hectometer
    :return: converted to meters
    """
    return x * 100


def kilometer_to_meter(x):
    """
    Function to convert kilometer to meter
    :param x: input in kilometer
    :return: converted to meters
    """
    return x * 1000


def inch_to_meter(x):
    """
    Function to convert inch to meter
    :param x: input in inches
    :return: converted to meters
    """
    return 2.54 * math.pow(10, -2)


def foot_to_meter(x):
    """
    Function to convert foot to meter
    :param x: input in foot
    :return: converted to meters
    """
    return x * 0.3048


def yard_to_meter(x):
    """
    Function to convert yard to meter
    :param x: input in yard
    :return: converted to meter
    """
    return x * 0.9144


def mile_to_meter(x):
    """
    Function to convert mile to meter
    :param x: input in mile
    :return: converted to meter
    """
    return 1.609344 * kilometer_to_meter(x)
