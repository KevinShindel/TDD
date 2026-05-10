from hypothesis import given
from hypothesis.strategies import floats
import numpy as np

from Ch03 import activation


@given(floats())
def test_relu(n):
    """ given is decorator that provides a value,
        floats - generate a float value
        activation - run some logic and return value
    """
    print(n)
    v = activation.relu(n)
    if not np.isnan(n):
        assert v >= 0
