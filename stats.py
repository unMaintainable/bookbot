def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        book_text = f.read()
        f.close()
    return book_text

def get_num_words(path):
    return len(get_book_text(path).split())

def get_num_chars(path):
    text = get_book_text(path).lower()
    chars_dict = {}
    for c in text:
        if c not in chars_dict:
            chars_dict[c] = 0
        chars_dict[c] += 1
    return chars_dict

def sort_on(items):
    return items["num"]

def sort_chars_dict(path):
    counted_chars_list = []
    for k, v in get_num_chars(path).items():
        if k.isalpha():
            counted_chars_list.append({"char": k, "num": v})
    counted_chars_list.sort(reverse=True, key=sort_on)
    return counted_chars_list