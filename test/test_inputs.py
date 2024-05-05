
from datetime import datetime

from pytest import MonkeyPatch

from inputs import in_amount, in_cat, in_date, in_entry, in_entry_index
from models import Entry


def test_index(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda x: "3")
    assert in_entry_index(4) == 3
    assert in_entry_index(2) is None

    monkeypatch.setattr("builtins.input", lambda x: "str")
    assert in_entry_index(4) is None


def test_date(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda x: "2024-05-05")
    assert isinstance(in_date(), datetime)

    monkeypatch.setattr("builtins.input", lambda x: "foo")
    assert in_date() is None


def test_amount(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda x: "100")
    assert in_amount() == 100

    monkeypatch.setattr("builtins.input", lambda x: "-100")
    assert in_amount() == -100

    monkeypatch.setattr("builtins.input", lambda x: "0")
    assert in_amount() == 0

    monkeypatch.setattr("builtins.input", lambda x: "str")
    assert in_amount() is None


def test_entry(monkeypatch: MonkeyPatch):
    fake = iter(["2024-05-05", "100", "str"])
    monkeypatch.setattr("builtins.input", lambda msg: next(fake))
    assert isinstance(in_entry(), Entry)


def test_cat(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("builtins.input", lambda x: "+")
    assert in_cat() is True

    monkeypatch.setattr("builtins.input", lambda x: "-")
    assert in_cat() is False

    monkeypatch.setattr("builtins.input", lambda x: "str")
    assert in_cat() is None
