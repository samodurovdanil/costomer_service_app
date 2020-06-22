word_list = ['attribute', 'класс', 'функция', 'type']

for i in word_list:
    bytes_word = bytes(i, encoding='utf-8')
    print(bytes_word, type(bytes_word))