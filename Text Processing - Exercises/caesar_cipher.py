text = input()
encrypted_text = ""
for char in text:
    char_ascii = ord(char)
    encrypted_char_ascii = char_ascii + 3
    encrypted_text += chr(encrypted_char_ascii)
print(encrypted_text)
