string = input().split()
total_sum = 0
for word in string:
    first_letter = word[0]
    last_letter = word[-1]
    digit = int(word[1:len(word) - 1])
    if first_letter.isupper():
        letter_position_alphabet = ord(first_letter) - 64
        total_sum += digit / letter_position_alphabet
    elif first_letter.islower():
        letter_position_alphabet = ord(first_letter) - 96
        total_sum += digit * letter_position_alphabet
    if last_letter.isupper():
        letter_position_alphabet = ord(last_letter) - 64
        total_sum -= letter_position_alphabet
    elif last_letter.islower():
        letter_position_alphabet = ord(last_letter) - 96
        total_sum += letter_position_alphabet
print(f"{total_sum:.2f}")
