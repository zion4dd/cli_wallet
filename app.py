from db import load_data, save_data
from menu import mainmenu

if __name__ == "__main__":
    book = load_data()
    mainmenu(book)
    save_data(book)
