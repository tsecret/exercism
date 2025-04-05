def egg_count(display_value: int):

    bits = []

    while display_value != 0:
      bits.append(display_value % 2)
      display_value = display_value // 2

    return bits.count(1)
