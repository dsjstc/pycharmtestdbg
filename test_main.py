import pytest
from main import *

@pytest.fixture
def deeptree():
    return 1


def test_foo():
    assert foo() == 'foo'


def test_bar():
    assert bar() == 'bar'