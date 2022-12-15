char_1 = input()
char_2 = input()


def characters_in_range(a, b):
    for character in range(ord(a) + 1, ord(b)):
        print(chr(character), end=" ")


characters_in_range(char_1, char_2)
