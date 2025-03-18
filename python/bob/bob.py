def isCapital(text: str) -> bool:

  word = [char for char in text if char.isalpha()]

  if len(word) == 0:
    return False

  for char in word:
    if char.islower():
      return False

  return True

def response(text: str):
    text = text.strip()

    if len(text) == 0:
      return 'Fine. Be that way!'
    elif isCapital(text) and text.endswith('?'):
      return 'Calm down, I know what I\'m doing!'
    elif isCapital(text):
      return 'Whoa, chill out!'
    elif text.endswith('?'):
      return 'Sure.'
    else:
      return 'Whatever.'
