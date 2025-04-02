def is_paired(input_string: str) -> bool:

  s = []

  CLOSING = ['}', ')', ']']
  OPENING = ['{', '(', '[']

  for char in input_string:

      if char in CLOSING and len(s) == 0:
        return False

      if char in OPENING:
        s.append(char)

      if char == ']':
          if s.pop() != '[':
            return False

      if char == ')':
          if s.pop() != '(':
            return False

      if char == '}':
          if s.pop() != '{':
            return False

  return len(s) == 0
