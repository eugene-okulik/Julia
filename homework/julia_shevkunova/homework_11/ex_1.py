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

print('Название: ', book_1.title, '|', 'Автор: ', book_1.author, '|', 'Страниц: ', book_1.number_of_pages, '|',
      'ISBN: ', book_1.ISBN, '|', 'Текст: ', book_1.text, '|', 'Материал: ', book_1.page_material, '|',
      'Зарезервировано: ', book_1.reserved)
print('Название: ', book_2.title, '|', 'Автор: ', book_2.author, '|', 'Страниц: ', book_2.number_of_pages, '|',
      'ISBN: ', book_2.ISBN, '|', 'Текст: ', book_2.text, '|', 'Материал: ', book_2.page_material, '|',
      'Зарезервировано: ', book_2.reserved)
print('Название: ', book_3.title, '|', 'Автор: ', book_3.author, '|', 'Страниц: ', book_3.number_of_pages, '|',
      'ISBN: ', book_3.ISBN, '|', 'Текст: ', book_3.text, '|', 'Материал: ', book_3.page_material, '|',
      'Зарезервировано: ', book_3.reserved)
print('Название: ', book_4.title, '|', 'Автор: ', book_4.author, '|', 'Страниц: ', book_4.number_of_pages, '|',
      'ISBN: ', book_4.ISBN, '|', 'Текст: ', book_4.text, '|', 'Материал: ', book_4.page_material, '|',
      'Зарезервировано: ', book_4.reserved)
print('Название: ', book_5.title, '|', 'Автор: ', book_5.author, '|', 'Страниц: ', book_5.number_of_pages, '|',
      'ISBN: ', book_5.ISBN, '|', 'Текст: ', book_5.text, '|', 'Материал: ', book_5.page_material, '|',
      'Зарезервировано: ', book_5.reserved)


class SchoolBook(Book):

    def __init__(self, title, author, number_of_pages, isbn, reserved, subject, school_class, presence_of_tasks):
        super().__init__(title, author, number_of_pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.presence_of_tasks = presence_of_tasks


math_book = SchoolBook('Алгебра', 'Кончаковский', 234, '3787D', False, 'Математика', 5, True)
physics_book = SchoolBook('Оптика', 'Петруня', 222, '3737D', True, 'Физика', 5, True)

print('Название: ', math_book.title, '|', 'Автор: ', math_book.author, '|', 'Страниц: ', math_book.number_of_pages, '|',
      'ISBN: ', math_book.ISBN, '|', 'Текст: ', math_book.text, '|', 'Материал: ', math_book.page_material, '|',
      'Зарезервировано: ', math_book.reserved, '|', 'Предмет: ', math_book.subject, '|', 'Класс: ',
      math_book.school_class, '|', 'Наличие заданий: ', math_book.presence_of_tasks)

print('Название: ', physics_book.title, '|', 'Автор: ', physics_book.author, '|', 'Страниц: ',
      physics_book.number_of_pages, '|',
      'ISBN: ', physics_book.ISBN, '|', 'Текст: ', physics_book.text, '|', 'Материал: ', physics_book.page_material,
      '|',
      'Зарезервировано: ', physics_book.reserved, '|', 'Предмет: ', physics_book.subject, '|', 'Класс: ',
      physics_book.school_class, '|', 'Наличие заданий: ', physics_book.presence_of_tasks)
