def recite(start: int, take=1):
    l = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

    song = []

    for i in range(start, start-take, -1):

      for _ in range(2):
          song.append(f"{l[i-1]} green bottle{'s' if i > 1 else ''} hanging on the wall,")

      song.append(f"And if one green bottle should accidentally fall,",)

      if i-1 >= 1:
        song.append(f"There'll be {l[i-2].lower()} green bottle{'s' if i-1 > 1 else ''} hanging on the wall.",)
      else:
        song.append(f"There'll be no green bottles hanging on the wall.",)

      if i != start-take+1:
        song.append("")

    return song
