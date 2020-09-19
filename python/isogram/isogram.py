def is_isogram(string):
    # string is all lower case
    string = string.lower()

    # Searching for the repeated strings
    existing = []
    for _str in string:
        if _str != ' ' and _str != '-':
            if _str in existing:
                return False
            else:
                existing.append(_str)

    return True
