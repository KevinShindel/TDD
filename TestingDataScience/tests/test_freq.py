import numpy as np
from hypothesis import given
from hypothesis.extra.numpy import arrays
from hypothesis.strategies import integers

from Ch03.freq import first_digit_freq

strategy = arrays(  # that's provide schema and data
    dtype=np.int64,  # type of data
    shape=integers(min_value=1, max_value=10_000),  # min and max values
    elements=integers(min_value=0, max_value=np.iinfo(np.int64).max - 1),  # max iteration times 9223372036854775806
)


@given(strategy)
def test_freq(values):
    """ gives provide data to test_freq , """
    freqs = first_digit_freq(values)
    assert freqs.shape == (10,)
    assert ((freqs >= 0) & (freqs <= 1)).all()
    assert np.allclose(freqs.sum(), 1)
