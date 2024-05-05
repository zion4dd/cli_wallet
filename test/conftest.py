import pytest

from models import Book


@pytest.fixture(scope="session")
def book():
    return Book()


# with pytest.raises(IndexError):
