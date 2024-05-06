from db import load_data, save_data
from menu import mainmenu

if __name__ == "__main__":
    book = load_data()
    mainmenu(book)
    save_data(book)


# book.add_entry(Entry("2024-01-01", True, 1000, "1st"))
# book.add_entry(Entry("2024-02-02", False, 500, "2nd"))
