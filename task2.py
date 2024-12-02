# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.44 #Мб
pages = 100
strings = 50
symbols = 25
one_code_symbol = 4 #Б

disk_mb = disk * 1024 * 1024 #Б в МБ
all_symbols = pages * strings * symbols #символов в книге
volume_all_symbols = one_code_symbol * all_symbols #объем в байтах
books = int (disk_mb // volume_all_symbols)

print("Количество книг, помещающихся на дискету:", books)