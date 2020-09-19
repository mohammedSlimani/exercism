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


'''
This is a smarter way of doing it! filter the string and then use the fact that sets have unique elements
def is_isogram(string):
    string = [char for char in string.lower() if char.isalnum()]
    return len(set(string)) == len(string)
'''