def is_isogram(string: str):

    s = set()

    for char in string:
      if char.isalpha():
        if char.lower() in s:
          return False

        s.add(char.lower())


    return True
