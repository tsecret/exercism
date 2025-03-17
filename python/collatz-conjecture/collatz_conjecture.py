def steps(number: int, step: int = 0):
  if number < 1:
    raise ValueError("Only positive integers are allowed")

  if number == 1:
    return step

  if number % 2 == 0:
    return steps(number / 2, step + 1)
  else:
    return steps(number * 3 + 1, step + 1)
