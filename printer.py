from datetime import datetime

from models import Book, Entry


def formatter_oneline(id, date, cat, amount, note):
    "Формирует однострочный вывод"

    return "# {0:6} | {1:10} | {2:10} | {3:15} | {4}".format(
        id, date, cat, amount, note
    )


def formatter_multiline(id, date, cat, amount, note):
    "Формирует многострочный вывод"

    return f"""#: {id}
Дата: {date}
Категория: {cat}
Сумма: {amount}
Описание: {note}
"""


def serializer(id, entry: Entry, *, oneline=False) -> str:
    "Сериализует объект записи для вывода"

    date = datetime.strftime(entry.date, "%Y-%m-%d")
    cat = "Доход" if entry.cat else "Расход"

    if oneline:
        return formatter_oneline(id, date, cat, entry.amount, entry.note)

    return formatter_multiline(id, date, cat, entry.amount, entry.note)


def printer(ls: list) -> None:
    "Выводит записи из списка через сериализатор"

    for i, e in enumerate(ls):
        print(serializer(i, e))


def printer_oneline(ls: list):
    "Компактно выводит записи из списка через сериализатор"

    print(formatter_oneline("id", "Дата", "Категория", "Сумма", "Описание"))
    for i, e in enumerate(ls):
        print(serializer(i, e, oneline=True))


def print_balance(book: Book):
    "Выводит баланс, доходы, расходы"

    print(
        f"Баланс: {book.get_balance()}",
        f"Доходы: {book.get_income()}",
        f"Расходы: {book.get_expences()}",
        sep="\n",
    )
