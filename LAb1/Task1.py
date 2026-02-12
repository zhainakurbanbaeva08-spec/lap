#1
def analyze_text(text):
    vowels=set("aeiouyаеёиоуыэюя")

    cleaned=""
    for ch in text.lower():
        if ch.isalpha() or ch==" ":
            cleaned=cleaned+ch

    unique_vowels=set()
    for ch in cleaned:
        if ch in vowels:
            unique_vowels.add(ch)

    words=cleaned.split()

    result_words=[]
    seen=set()
    for word in words:
        if (len(word) >=5 and
            word[0] == word[-1] and
            word not in seen):
            result_words.append(word)
            seen.add(word)

     return (len(unique_vowels), " ".join(result_words))