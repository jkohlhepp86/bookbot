def word_count(book_string):
    num_words = len(book_string.split())
    return num_words


def char_count(book_string):
    lowered_string = book_string.lower()
    count_each_char = {}
    for char in lowered_string:
        if char not in count_each_char:
            count_each_char[char] = 1
        else:
            count_each_char[char] += +1
    return count_each_char

def order_count(dict_sort):
    chars_list = []

    for char, count in dict_sort.items():
        chars_list.append({"char": char, "count": count})

    chars_list.sort(reverse=True, key=lambda x: x["count"])
    return chars_list
