import menu
from db import load_data, save_data
from inputs import in_amount, in_cat, in_date, in_entry, in_entry_index
from models import Book
from printer import print_balance, printer


def menu_1() -> None:
    print_balance(B)

    # Вариант с выбором вывода:
    # i = input(menu.str_1)
    # match i:
    #     case "1":
    #         print("Баланс:", B.get_balance())
    #     case "2":
    #         print("Доходы:", B.get_income())
    #     case "3":
    #         print("Расходы:", B.get_expences())


def menu_2():
    entry = in_entry("Добавление новой записи.")
    if entry:
        B.add_entry(entry)


def menu_3():
    i = input(menu.str_2)
    match i:
        case "1":
            printer(B.get_all())

        case "2":
            n = in_entry_index(len(B))
            if n:
                entry = in_entry("Редактирование записи.")
                if entry:
                    B[n] = entry


def menu_4():
    i = input(menu.str_4)
    match i:
        case "1":
            cat = in_cat()
            if cat:
                printer(B.getby_income())
            if cat is False:
                printer(B.getby_expences())
            if cat is None:
                print("Неизвестная категория.")

        case "2":
            date = in_date()
            if date:
                printer(B.getby_date(date))

        case "3":
            amount = in_amount()
            if amount:
                printer(B.getby_amount(abs(amount)))


def mainmenu():
    while True:
        i = input(menu.str_main)
        match i:
            case "1":
                menu_1()
            case "2":
                menu_2()
            case "3":
                menu_3()
            case "4":
                menu_4()
            case "q":
                return
            case _:
                print("invalid input")


if __name__ == "__main__":
    B: Book = load_data()
    mainmenu()
    # B.sort_book()
    save_data(B)


# B.add_entry(Entry("2024-05-02", True, 1000, "1st"))
# B.add_entry(Entry("2024-05-02", False, 500, "2nd"))
