def translate(text: str):

    vowels = ['a', 'e', 'i', 'o', 'u']

    if text[0] in vowels or text[0] == 'xr' or text[0] == 'ay':
      return text + 'ay'

    temp_consonants = []

    for char in text:

      if char == 'u' and temp_consonants[-1] == 'q':
        return text[len(temp_consonants):] + ''.join(temp_consonants) + 'uay'

      if char == 'y':
        return text[len(temp_consonants):] + 'ay'

      temp_consonants.append(char)
