def check_for_triangle(a: int, b: int, c:int):
  if a + b < c or a + c < b or b + c < a:
    return False
  return True
