def rotate(text: str, key: int):
    alph = 'abcdefghijklmnopqrstuvwxyz'

    text = list(text)

    for i, char in enumerate(text):

      if not char.isalpha():
        continue

      idx = alph.index(char.lower())

      text[i] = alph[(idx + key) % 26].upper() if char.isupper() else alph[(idx + key) % 26]

    return ''.join(text)
