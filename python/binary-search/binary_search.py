from typing import List

def find(search_list: List[int], value: int):
    l = 0
    r = len(search_list) - 1

    while l <= r:
      mid = (l + r) // 2

      if search_list[mid] == value:
        return mid

      if search_list[mid] > value:
        r = mid - 1
      else:
        l = mid + 1

    raise ValueError("value not in array")
