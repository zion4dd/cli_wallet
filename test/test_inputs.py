from datetime import datetime

import pytest
from pytest import MonkeyPatch

from inputs import in_amount, in_cat, in_date, in_entry, in_entry_index
from models import Entry


@pytest.mark.parametrize(
    "len, inp, expect",
    (
        (4, "3", 3),
        (2, "3", None),
        (4, "str", None),
    ),
)
def test_index(monkeypatch: MonkeyPatch, len, inp, expect):
    monkeypatch.setattr("builtins.input", lambda x: inp)
    assert in_entry_index(len) == expect


@pytest.mark.parametrize(
    "inp, expect",
    (
        ("2024-05-05", datetime.strptime("2024-05-05", "%Y-%m-%d")),
        ("2024-05-XX", None),
        ("str", None),
    ),
)
def test_date(monkeypatch: MonkeyPatch, inp, expect):
    monkeypatch.setattr("builtins.input", lambda x: inp)
    assert in_date() == expect


@pytest.mark.parametrize(
    "inp, expect",
    (
        ("100", 100),
        ("-100", -100),
        ("0", 0),
        ("str", None),
    ),
)
def test_amount(monkeypatch: MonkeyPatch, inp, expect):
    monkeypatch.setattr("builtins.input", lambda x: inp)
    assert in_amount() == expect


@pytest.mark.parametrize(
    "ls, expect",
    (
        (["2024-05-05", "100", "str"], Entry("2024-05-05", True, 100, "str")),
        (["2024-05-XX", "100", "str"], None),
        (["2024-05-05", "XX", "str"], None),
    ),
)
def test_entry(monkeypatch: MonkeyPatch, ls, expect):
    fake = iter(ls)
    monkeypatch.setattr("builtins.input", lambda msg: next(fake))
    assert in_entry() == expect


@pytest.mark.parametrize(
    "inp, expect",
    (
        ("+", True),
        ("-", False),
        ("str", None),
    ),
)
def test_cat(monkeypatch: MonkeyPatch, inp, expect):
    monkeypatch.setattr("builtins.input", lambda x: inp)
    assert in_cat() == expect
