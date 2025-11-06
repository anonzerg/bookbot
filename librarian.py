def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_each_char(text):
    d = {}
    for c in text.lower():
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    return d

def dict_to_list(d):
    l = []
    for k, v in d.items():
        if k.isalpha():
            l.append({"char": k, "num": v})

    return l

def sort_on(d):
    return d["num"]

def sort_dict(d):
    l = dict_to_list(d)
    l.sort(reverse=True, key=sort_on)
    return l
