from typing import List

def find_anagrams(word: str, candidates: List[str]):
    anagrams = []

    for candidate in candidates:
      if len(word) != len(candidate) or word.lower() == candidate.lower():
        continue

      s = list(word.lower())

      for char in candidate.lower():

        if char in s:
          s.remove(char)
        else:
          break


      if len(s) == 0:
        anagrams.append(candidate)





    return anagrams
