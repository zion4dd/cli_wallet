import pytest

from models import Book, Entry


@pytest.fixture(scope="session")
def book():
    return Book()


@pytest.fixture  # (scope="session")
def e1():
    return Entry("2024-01-01", True, 1000, "1st")


@pytest.fixture  # (scope="session")
def e2():
    return Entry("2024-02-02", False, 300, "2st")


@pytest.fixture  # (scope="session")
def e3():
    return Entry("2024-03-03", False, 500, "3st")


# with pytest.raises(IndexError):
# pytest --cov --cov-report html
