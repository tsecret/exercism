def is_valid(isbn: str):

    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
      return False

    sum = 0

    for i in range(10, 0, -1):

      if not isbn[10-i].isdigit() and isbn[10-i] != 'X':
        return False

      if isbn[10-i] == 'X':
        if i != 1:
          return False

        sum += 10 * i
        continue

      sum += int(isbn[10-i]) * i

    return sum % 11 == 0
