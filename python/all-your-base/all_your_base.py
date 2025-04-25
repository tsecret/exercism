from typing import List

def rebase(input_base: int, digits: List[int], output_base: int):

    if input_base < 2:
      raise ValueError("input base must be >= 2")

    for digit in digits:
      if 0 <= digit < input_base:
        continue
      else:
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
      raise ValueError("output base must be >= 2")

    # 42 base 10 = (4 × 10¹) + (2 × 10⁰)
    # 101010 base 2 = (1 × 2⁵) + (0 × 2⁴) + (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)

    # 101 base 2 = (1 x 2^2) + (0 x 2^1) + (1 x 2^0)
    # 1120 base 3 = (1 x 3^3) + (1 x 3^2) + (2 x 3^1) + (0 x 3^0)

    # 2 10 base 16 = (2 & 16^1) + (10 * 16)
    # 42 =  1 * 16 ^ 1


    sum = 0
    output = []

    for i, digit in enumerate(reversed(digits)):
      sum += digit * (input_base ** i)

    if output_base >= sum:
      return [sum / output_base]

    i = 1 # digit
    j = 0 # power

    while sum > 0:

      print('Sum', sum)


      if output_base >= sum:
        output.append(i)
        break

      while i * (output_base ** (j+1)) < sum:
        print(i * (output_base ** j+1))
        j += 1

      while (i+1) * (output_base ** j) < sum:
        (i+1) * (output_base ** j)
        i += 1

      n = i * (output_base ** j)

      output.append(i)
      sum -= n
      i = 1
      j = 0




    return output
