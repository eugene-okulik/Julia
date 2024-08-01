class Book:
    page_material = 'paper'
    text = True

    def __init__(self, title, author, number_of_pages, isbn, reserved):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = isbn
        self.reserved = reserved


book_1 = Book('Наука и техника', 'Кончаковский', 234, '3745FD', False)
book_2 = Book('Ваша Усадьба', 'Мизаловский', 433, '37455FD', True)
book_3 = Book('Мир животных', 'Лизанков', 433, '3745JF', False)
book_4 = Book('Сказки добрых людей', 'Чеченко', 433, '375FD', False)
book_5 = Book('Здоровое питание', 'Шебашкович', 123, '1245FD', False)


def descr_of_books(book):
    if book.reserved is True:
        print('Название: ', book.title, '|', 'Автор: ', book.author, '|', 'Страниц: ', book.number_of_pages, '|',
              'ISBN: ', book.ISBN, '|', 'Текст: ', book.text, '|', 'Материал: ', book.page_material, '|',
              'Зарезервировано: ', book.reserved)
    else:
        print('Название: ', book.title, '|', 'Автор: ', book.author, '|', 'Страниц: ', book.number_of_pages, '|',
              'ISBN: ', book.ISBN, '|', 'Текст: ', book.text, '|', 'Материал: ', book.page_material)


descr_of_books(book_1)
descr_of_books(book_2)
descr_of_books(book_3)
descr_of_books(book_4)
descr_of_books(book_5)


class SchoolBook(Book):

    def __init__(self, title, author, number_of_pages, isbn, reserved, subject, school_class, presence_of_tasks):
        super().__init__(title, author, number_of_pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.presence_of_tasks = presence_of_tasks


math_book = SchoolBook('Алгебра', 'Кончаковский', 234, '3787D', False, 'Математика', 5, True)
physics_book = SchoolBook('Оптика', 'Петруня', 222, '3737D', True, 'Физика', 5, True)


def descr_of_books(book):
    if book.reserved is True:
        print('Название: ', book.title, '|', 'Автор: ', book.author, '|', 'Страниц: ', book.number_of_pages, '|',
              'ISBN: ', book.ISBN, '|', 'Текст: ', book.text, '|', 'Материал: ', book.page_material, '|',
              'Зарезервировано: ', book.reserved, '|', 'Предмет: ', book.subject, '|', 'Класс: ',
              book.school_class, '|', 'Наличие заданий: ', book.presence_of_tasks)
    else:
        print('Название: ', book.title, '|', 'Автор: ', book.author, '|', 'Страниц: ', book.number_of_pages, '|',
              'ISBN: ', book.ISBN, '|', 'Текст: ', book.text, '|', 'Материал: ', book.page_material, '|', 'Предмет: ',
              book.subject, '|', 'Класс: ',
              book.school_class, '|', 'Наличие заданий: ', book.presence_of_tasks)


descr_of_books(physics_book)
descr_of_books(math_book)
