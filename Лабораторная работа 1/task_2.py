one_symbol_size_b = 4
disk_size_mb = 1.44
disk_size_b = disk_size_mb * 1024 * 1024  # Перевод из Мб в байты

pages = 100
lines = 50
symbols = 25

one_book_size = pages * lines * symbols * one_symbol_size_b
num_books = int(disk_size_b // one_book_size)
print("Количество книг, помещающихся на дискету:", num_books)
