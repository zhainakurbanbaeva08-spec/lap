#2
process=lambda s: " ".join(
    filter(
        lambda word: len(word)%2==0,
        map(
            lambda word: word[::-1],
            filter(lambda word: not any (ch.isdigit()for ch in word), s.split())
        )
    )
)