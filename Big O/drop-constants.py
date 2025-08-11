# It will be n + n = 2n operations, but we drop constants in Big O notation.
# Therefore, the time complexity is O(n).
# We drop constants in Big O notation, so the time complexity remains O(n). Like this: n(100n) = O(n), not O(100n).

def print_items(n):
   for i in range(n):
      print(i)
      
   for j in range(n):
      print(j)
      
print_items(5)
