from datetime import datetime

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class Entry:
    "Объект записи кошелька"

    date: datetime
    cat: bool
    amount: int
    note: str


@dataclass
class Book:
    "Содержит список объектов(записей) кошелька. Методы добавляющие и изменяющие записи вызывают сортировку."

    entries: list[Entry] = Field(default_factory=list)

    def __getitem__(self, key: int):
        return self.entries[key]

    def __setitem__(self, key: int, value: Entry):
        self.entries[key] = value
        self.sort_book()

    def __len__(self):
        return len(self.entries)

    def sort_book(self):
        self.entries.sort(key=lambda x: x.date, reverse=True)

    def add_entry(self, entry: Entry):
        self.entries.append(entry)
        self.sort_book()

    def get_all(self):
        return self.entries

    def get_income(self):
        return sum([entry.amount for entry in self.entries if entry.cat])

    def get_expences(self):
        return sum([entry.amount for entry in self.entries if not entry.cat])

    def get_balance(self):
        return self.get_income() - self.get_expences()

    def getby_date(self, date: datetime):
        return [entry for entry in self.entries if entry.date == date]

    def getby_income(self):
        return [entry for entry in self.entries if entry.cat]

    def getby_expences(self):
        return [entry for entry in self.entries if not entry.cat]

    def getby_amount(self, amount: int):
        return [entry for entry in self.entries if entry.amount == amount]
