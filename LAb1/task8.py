vowels = "aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ"

func8 = lambda s: " ".join(
    map(
        lambda word:
            word if any(ch.isdigit() for ch in word)
            else ("VOWEL" if word[0] in vowels else "CONSONANT"),
        s.split()
    )
)