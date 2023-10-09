import math

def test_logarithms():
    random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_logarithms = [0.0, 0.6931471805599453, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003, 1.791759469228055, 1.9459101490553132, 2.0794415416798357, 2.1972245773362196, 2.302585092994046]
    computed_logarithms = [math.log(num) for num in random_numbers]
    assert computed_logarithms == expected_logarithms, f"Expected {expected_logarithms}, but got {computed_logarithms}"