def is_armstrong_number(number: int):

    sum = 0
    number_as_str = str(number)
    power = len(number_as_str)

    for digit in number_as_str:
      sum += int(digit) ** power

    return sum == number
