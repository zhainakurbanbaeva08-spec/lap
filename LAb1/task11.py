def common_unique_chars(s1, s2):
    result = ""
    seen = set()

    for ch in s1:
        if (
                ch not in seen and
                ch in s2 and
                not ch.isdigit() and
                ch != " "
        ):
            result += ch
            seen.add(ch)

    return result