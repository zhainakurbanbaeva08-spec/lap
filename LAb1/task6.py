func6 = lambda s: list(
    filter(
        lambda word: (
            len(set(word.lower())) == len(word) and
            not any(ch.isdigit() for ch in word)
        ),
        filter(lambda w: len(word) >= 4, s.split())
    )
)