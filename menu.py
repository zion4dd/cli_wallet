from inputs import in_amount, in_cat, in_date, in_entry, in_entry_index
from models import Book
from printer import print_balance, printer, printer_oneline

main = """
1. Вывод баланса, доходов и расходов.
2. Добавление новой записи о доходе или расходе.
3. Просмотр и изменение существующих записей о доходах и расходах.
4. Поиск записей по категории, дате или сумме.
q. quit
"""

s1 = """
1. Показать текущий баланс
2. Показать доходы
3. Показать расходы
"""

s2 = """
1. Отобразить записи
2. Редактировать записи
"""

s4 = """
1. Поиск по катергории
2. Поиск по дате
3. Поиск по сумме
"""


def menu_1(book: Book) -> None:
    "Вывод баланса"

    print_balance(book)

    # Вариант с выбором вывода:
    # i = input(s1)
    # match i:
    #     case "1":
    #         print("Баланс:", book.get_balance())
    #     case "2":
    #         print("Доходы:", book.get_income())
    #     case "3":
    #         print("Расходы:", book.get_expences())


def menu_2(book: Book):
    "Меню добавления новой записи."

    entry = in_entry("Добавление новой записи.")
    if entry:
        book.add_entry(entry)


def menu_3(book: Book):
    "Меню редактирования записей."

    i = input(s2)
    match i:
        case "1":
            printer(book.get_all())

        case "2":
            printer_oneline(book.get_all())
            n = in_entry_index(len(book))
            if n:
                entry = in_entry("Редактирование записи.")
                if entry:
                    book[n] = entry


def menu_4(book: Book):
    "Меню поиска."

    i = input(s4)
    match i:
        case "1":
            cat = in_cat()
            if cat:
                printer(book.getby_income())
            if cat is False:
                printer(book.getby_expences())
            if cat is None:
                print("Неизвестная категория.")

        case "2":
            date = in_date()
            if date:
                printer(book.getby_date(date))

        case "3":
            amount = in_amount()
            if amount:
                printer(book.getby_amount(abs(amount)))


def mainmenu(book: Book):
    "Основное меню."

    while True:
        i = input(main)
        match i:
            case "1":
                menu_1(book)
            case "2":
                menu_2(book)
            case "3":
                menu_3(book)
            case "4":
                menu_4(book)
            case "q":
                return
            case _:
                print("invalid input")
