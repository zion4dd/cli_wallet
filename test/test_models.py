from models import Book, Entry


def test_add(book: Book):
    "добавление записей и сортировка по убыванию"

    e1 = Entry("2024-01-01", True, 1000, "1st")
    e2 = Entry("2024-02-02", False, 300, "2st")
    book.add_entry(e1)
    book.add_entry(e2)
    assert e1 in book and e2 in book
    assert book[0] is e2
    assert book[1] is e1


def test_balance(book: Book):
    "баланс, доход, расход"

    assert book.get_balance() == 700
    assert book.get_income() == 1000
    assert book.get_expences() == 300


def test_edit(book: Book):
    "редактирование записи"

    e3 = Entry("2024-03-03", False, 500, "2st")
    book[1] = e3
    assert e3 in book
    assert book[0] is e3
