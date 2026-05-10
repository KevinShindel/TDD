from os import environ

import pytest

in_ci = 'CI' in environ  # CI condition tests
ci_only = pytest.mark.skipif(not in_ci, reason='not in CI')  # NOT CI condition tests


def test_always():
    pass


@ci_only
def test_in_ci():
    pass


@pytest.mark.web
def test_web():
    pass
