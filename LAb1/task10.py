func10 = lambda s: sum(
    1 for word in s.split()
    if (
        any(ch.isdigit() for ch in word) and
        not word[0].isdigit() and
        len(word) >= 5
    )
)