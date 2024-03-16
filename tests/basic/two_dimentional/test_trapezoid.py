from formulas.basic.two_dimentional import trapezoid


def test_area_trapezoid():
    assert trapezoid.area(13.67, 44.76, 34.8) == 1016.6819999999999
