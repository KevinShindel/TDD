from pathlib import Path

import pytest
import yaml

from Ch02.splitter import split_to_chunks

here = Path(__file__).absolute().parent.parent / 'data'


def load_split_cases():
    """ function that reads data from yaml files and return data """
    cases_file = here / 'split_cases.yml'
    with cases_file.open() as fp:
        data = yaml.safe_load(fp)

    for tc in data:
        yield tc['size'], tc['chunk_size'], tc['chunks']


@pytest.mark.parametrize('size, chunk_size, expected', load_split_cases())
def test_split_to_chunks(size, chunk_size, expected):
    chunks = split_to_chunks(size, chunk_size)
    # split_to_chunks returns tuples generator, test case has lists
    chunks = [list(c) for c in chunks]
    assert chunks == expected


@pytest.mark.parametrize('size, chunk_size, expected', load_split_cases())
def test_splitter(size, chunk_size, expected):
    """ execute load_split_cases and provide args that returned (see the return from function ) """
    chunks = split_to_chunks(size, chunk_size)
    actual = list(map(list, chunks))
    assert actual == expected
