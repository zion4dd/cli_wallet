from models import Book, Entry


def test_add(book: Book, e1: Entry, e2: Entry):
    "добавление записей и сортировка по убыванию"

    book.add_entry(e1)
    book.add_entry(e2)
    assert e1 in book and e2 in book
    assert book[0] is e2
    assert book[1] is e1
    assert len(book) == 2


def test_getby(book: Book, e1: Entry, e2: Entry):
    "тест методов поиска записей по категории, дате или сумме"

    ls = book.get_all()
    assert e1 in ls and e2 in ls
    assert isinstance(ls, list) and len(ls) == 2

    ls = book.getby_date(e1.date)
    assert isinstance(ls, list) and len(ls) == 1

    ls = book.getby_amount(e1.amount)
    assert e1 in ls
    assert isinstance(ls, list) and len(ls) == 1

    ls = book.getby_income()
    assert e1 in ls
    assert isinstance(ls, list) and len(ls) == 1

    ls = book.getby_expences()
    assert e2 in ls
    assert isinstance(ls, list) and len(ls) == 1


def test_balance(book: Book):
    "баланс, доход, расход"

    assert book.get_balance() == 700
    assert book.get_income() == 1000
    assert book.get_expences() == 300


def test_edit(book: Book, e1, e3):
    "редактирование записи"

    book[1] = e3
    assert e3 in book
    assert e1 not in book
    assert book[0] is e3
