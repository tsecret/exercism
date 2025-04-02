def square_root(number: int):
    x = number


    while True:
      x = 0.5 * (x + number / x)

      if x * x == number:
        return x
