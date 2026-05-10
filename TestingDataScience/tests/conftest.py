from collections import namedtuple

import pytest
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

from Ch02.api_client import APIClient


def _get_model(clf):
    Model = namedtuple('Model', 'version clf')
    return Model(version='2022-03-24', clf=clf)


@pytest.fixture
def client():
    # setup
    client = APIClient('localhost')

    yield client

    # teardown
    client.close()


def _load_data():
    digits = load_digits()
    return digits['data'], digits['target']


@pytest.fixture
def regression_data():
    # TODO: Load from regression database
    Data = namedtuple('Data', 'version X y')

    X, y = _load_data()
    return Data(
        version='2022-02-17',
        X=X,
        y=y,
    )


@pytest.fixture
def pipeline_model():
    # TODO: Load model from model store

    X, y = _load_data()
    X_train, _, y_train, _ = train_test_split(X, y, random_state=123)

    clf = Pipeline(steps=[
        ('pca', PCA(n_components=10)),
        ('svc', SVC(random_state=353))
    ])

    clf.fit(X_train, y_train)

    return _get_model(clf)


@pytest.fixture
def forest_model():
    # TODO: Load model from model store
    X, y = _load_data()
    X_train, _, y_train, _ = train_test_split(X, y, random_state=123)

    clf = RandomForestClassifier(random_state=353)
    clf.fit(X_train, y_train)

    return _get_model(clf)
