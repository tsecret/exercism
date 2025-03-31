from typing import List

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

TOLERANCE = {
  "grey": 0.05,
  "violet": 0.1,
  "blue": 0.25,
  "green": 0.5,
  "brown": 1,
  "red": 2,
  "gold": 5,
  "silver": 10,
}

def resistor_label(colors: List[str]):

    if len(colors) == 1 and colors[0] == 'black':
      return '0 ohms'

    amount = 0
    prefix = ''

    tolerance = colors.pop()
    n_of_zeros = COLORS.index(colors.pop())
    amount = int("".join([str(COLORS.index(color)) for color in colors]))

    if n_of_zeros > 0:
      amount *= 10**n_of_zeros

    if amount // 1_000_000_000 >= 1:
      amount = amount / 1_000_000_000
      prefix = 'giga'

    elif amount // 1_000_000 >= 1:
      amount = amount / 1_000_000
      prefix = 'mega'

    elif amount // 1000 >= 1:
      amount = amount / 1_000
      prefix = 'kilo'

    return f'{amount:g} {prefix}ohms ±{TOLERANCE[tolerance]}%'
