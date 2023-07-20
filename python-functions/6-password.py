def validate_password(password):
    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isspace():
            return False
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
        if char.isdigit():
            has_digit = True

    return has_uppercase and has_lowercase and has_digit
