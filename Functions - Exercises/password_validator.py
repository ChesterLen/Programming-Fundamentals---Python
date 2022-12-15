def password_validation(password_):
    password_is_valid = True
    if len(password_) < 6 or len(password_) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False
    if not password_.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False
    dgt_counter = 0
    for x in password_:
        if x.isdigit():
            dgt_counter += 1
    if dgt_counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    return password_is_valid


password = input()
validation = password_validation(password)
if validation:
    print("Password is valid")
