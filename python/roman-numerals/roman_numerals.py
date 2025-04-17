def roman(number: int):
    # 9 => IX
    # 16 => XVI
    # 27 => XXVII
    # 48 => XLVIII
    # 49 => XLIX

    NUMBERS = [
      (1000, 'M'),
      (900, 'CM'),
      (500, 'D'),
      (400, 'CD'),
      (100, 'C'),
      (90, 'XC'),
      (50, 'L'),
      (40, 'XL'),
      (10, 'X'),
      (9, 'IX'),
      (5, 'V'),
      (4, 'IV'),
      (1, 'I'),
    ]

    roman = ''

    while number > 0:

      for representation in NUMBERS:
        if number >= representation[0]:
          roman += representation[1]
          number -= representation[0]
          break



    return roman
