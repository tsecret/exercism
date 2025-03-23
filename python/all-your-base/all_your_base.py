from typing import List

def rebase(input_base: int, digits: List[int], output_base: int):

    if input_base < 2:
      raise ValueError("input base must be >= 2")

    for d in digits:
      if d < 0 or d >= input_base:
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
      raise ValueError("output base must be >= 2")


    ans = []

    for i in range(len(digits)-1, -1, -1):
      print(i)

    return ans
