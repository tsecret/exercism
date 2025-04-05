def commands(binary_str: str):
    actions = []

    commands = ['reverse', 'jump', 'close your eyes', 'double blink' , 'wink' ]

    for i in range(len(binary_str)-1, -1, -1):
      if binary_str[i] != '1':
        continue

      if i == 0:
        actions.reverse()
      else:
        actions.append(commands[i])

    return actions
