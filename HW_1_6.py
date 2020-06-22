import locale
import subprocess

content_list = ['сетевое программирование', 'сокет', 'декоратор']
# создание файла с контентом
with open('test_file.txt', 'w') as f:
    for i in content_list:
        f.write(f'{i}\n')

# кодировка по умолчанию
def_coding = locale.getpreferredencoding()
print(def_coding)

# попытка чтения
with open('test_file.txt', ) as f:
    for i in f:
        print(i.encode('utf-8'), end='')