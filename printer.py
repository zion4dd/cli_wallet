from models import Book, Entry


def serializer(id, entry: Entry) -> str:
    "Сериализует объект записи в строчный формат вывода"

    cat = "Доход" if entry.cat else "Расход"
    strout = f"""
#: {id}
Дата: {entry.date}
Категория: {cat}
Сумма: {entry.amount}
Описание: {entry.note}
"""
    return strout


def printer(ls: list) -> None:
    "Выводит записи из списка через сериализатор"

    for i, e in enumerate(ls):
        print(serializer(i, e))


def print_balance(book: Book):
    "Выводит баланс, доходы, расходы"

    print(
        f"Баланс: {book.get_balance()}",
        f"Доходы: {book.get_income()}",
        f"Расходы: {book.get_expences()}",
        sep="\n",
    )
