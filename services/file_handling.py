import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    string = text[start::][:page_size]
    for i in reversed(range(len(string))):
        if string[i] in [',', '.', '!', ':', ';', '?']:
            return string[:i + 1], i + 1


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, "r", encoding='utf-8') as file:
        text = file.read()
    start, page_number = 0, 1
    while start < len(text):
        page_text, number = _get_part_text(text=text, start=start, page_size=PAGE_SIZE)
        start += number
        book[page_number] = page_text.strip()
        page_number += 1



# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))