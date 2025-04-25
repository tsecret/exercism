from typing import Dict, List

def transform(legacy_data: Dict[int, List[str]]):

    data = {}

    for point, letters in legacy_data.items():
      for letter in letters:
        data[letter.lower()] = point

    return data
