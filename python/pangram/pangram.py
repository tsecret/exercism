def is_pangram(sentence: str):


  d = set()

  for char in sentence:
    if char.isalpha():
      if char.lower() not in d:
        d.add(char.lower())

  print(d)

  return len(d) == 26
