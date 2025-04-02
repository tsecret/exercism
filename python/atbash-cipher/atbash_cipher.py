PLAIN = 'abcdefghijklmnopqrstuvwxyz'
CIPHER = 'zyxwvutsrqponmlkjihgfedcba'

def encode(plain_text: str):
    plain_text = "".join([char for char in plain_text.lower() if char.isalnum()])

    output = ''

    for i in range(1, len(plain_text)+1):

      if plain_text[i-1].isnumeric():
        output += plain_text[i-1]

      if plain_text[i-1].isalpha():
        output += CIPHER[PLAIN.index(plain_text[i-1])]

      if i % 5 == 0 and i != len(plain_text):
        output += ' '

    return output

def decode(ciphered_text: str):
    ciphered_text = ciphered_text.replace(' ', '')

    return "".join([PLAIN[CIPHER.index(char)] if char.isalpha() else char for char in ciphered_text])
