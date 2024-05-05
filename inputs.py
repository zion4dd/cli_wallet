from datetime import datetime

from models import Entry


def in_entry_index(len_book: int) -> int | None:
    "Ввод и валидация номера записи. len_book - длина объекта кошелька."

    n = input(f"Введите номер записи от 0 до {len_book-1}: ")
    try:
        n = int(n)
        if n not in range(len_book):
            raise IndexError
            
    except ValueError:
        print("Неверный формат!")
        return

    except IndexError:
        print("Данная запись не обнаружена.")
        return

    return n


def in_date() -> datetime | None:
    "Ввод и валидация даты"

    date = input("Введите дату в формате YYYY-MM-DD: ")
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Неверный формат!")
        return

    return date


def in_amount() -> int | None:
    "Ввод и валидация суммы"

    amount = input("Введите сумму (доход 100; расход -100): ")
    try:
        amount = int(amount)
    except ValueError:
        print("Неверный формат!")
        return

    return amount


def in_entry(startline="") -> Entry | None:
    "Ввод и валидация записи. startline - заголовок ввода."

    print(startline)
    date = in_date()
    if not date:
        return

    amount = in_amount()
    if not amount:
        return

    note = input("Введите описание: ")
    cat = True if amount >= 0 else False
    entry = Entry(date, cat, abs(amount), note)
    return entry


def in_cat() -> bool | None:
    "Ввод и валидация категории"

    cat = input("Введите знак доход или расход [+/-]: ").lower()
    if cat == "+":
        return True

    if cat == "-":
        return False
