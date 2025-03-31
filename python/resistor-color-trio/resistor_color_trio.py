from typing import List

def label(colors: List[str]):
    COLORS = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]

    colors = colors[:3]

    n_of_zeros = COLORS.index(colors.pop())
    amount = int("".join([str(COLORS.index(color)) for color in colors]))

    if n_of_zeros > 0:
      amount *= 10**n_of_zeros

    if amount // 1_000_000_000 >= 1:
      return str(amount // 1_000_000_000) + ' gigaohms'

    if amount // 1_000_000 >= 1:
      return str(amount // 1_000_000) + ' megaohms'

    if amount // 1000 >= 1:
      return str(amount // 1000) + ' kiloohms'


    return str(amount) + ' ohms'
