import os
import pickle
from contextlib import redirect_stdout

from models import Book
from printer import print_balance, printer


def load_data() -> Book:
    "Загрузка объекта кошелька из файла book.bin. Если файл не существует возвращает созданный объект кошелька"

    if os.path.exists("book.bin"):
        with open("book.bin", "rb") as file:
            return pickle.loads(file.read())

    return Book()


def save_data(book: Book) -> None:
    "Сохранение объекта кошелька в book.bin и сохранение записей через поток вывода в book.txt"

    # book.sort_book()
    with open("book.bin", "wb") as file:
        file.write(pickle.dumps(book))

    with open("book.txt", "w", encoding="utf-8") as f:
        with redirect_stdout(f):
            print_balance(book)
            print("\n======================================")
            printer(book.get_all())
