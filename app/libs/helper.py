
def is_isbn_or_key(word):
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些‘ - ’
    isbn_or_key = 'key'
    # 判断isbn13
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    
    short_word = word.replace('-', '')
    # 判断isbn10
    if '-' in word and short_word == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    
    return isbn_or_key
