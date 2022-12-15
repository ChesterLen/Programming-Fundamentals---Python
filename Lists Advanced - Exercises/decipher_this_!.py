def ord_to_chr(word):
    string = list(word)
    chr_string = []
    while string[0].isdigit():
        chr_string.append(string[0])
        string.pop(0)
    chr_ord = int("".join(chr_string))
    string.insert(0, chr(chr_ord))
    return "".join(string)
def switch_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return "".join(letters)
print(" ".join([switch_letters(ord_to_chr(word)) for word in input().split()]))
