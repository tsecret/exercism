def rows(letter: str):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    idx = LETTERS.find(letter)
    elements = idx * 2 + 1

    diamond = []

    for _ in range(elements):
      r = []
      for _ in range(elements):
        r.append(" ")
      diamond.append(r)

    l = idx
    r = idx
    u = 0
    b = elements - 1

    while u <= b:

        diamond[u][l] = LETTERS[u]
        diamond[u][r] = LETTERS[u]
        diamond[b][l] = LETTERS[u]
        diamond[b][r] = LETTERS[u]

        l -= 1
        r += 1
        u += 1
        b -= 1


    return ["".join(row) for row in diamond]
