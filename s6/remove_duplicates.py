def remove_consecutive_duplicates(string: str) -> str:
    if not string:
        return string

    result = [string[0]]
    for char in string[1:]:
        if char != result[-1]:
            result.append(char)

    return ''.join(result)
