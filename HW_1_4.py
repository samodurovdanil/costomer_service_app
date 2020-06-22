word_list = ['разработка', 'администрирование', 'protocol', 'standard']

for i in word_list:
    bytes_word = i.encode('utf-8')
    print(bytes_word, type(bytes_word))
    word = bytes_word.decode('utf-8')
    print(word, type(word))