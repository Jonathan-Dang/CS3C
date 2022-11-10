#   "%d"
number = 420
print(f"Number: {number}")

#   "%5d"
print(f"{number:>5}")

#   "%05d"
print(f"{number:>05}")

#   "Quantity:%5d"
print(f"Quantity:{number:>5}")

#   "%f"
number_2 = 1.23456789
print(f"{number_2}")

#   "%.2f"
print(f"{number_2:.3}")

#   "%7.2f"
print(f"{number_2:>7.3}")

#   "%s"
strings = "Hello"
print(f"{strings}")

#   "%d %.2f"
print(f"{number} {number_2:.3}")

#   "%9s"
print(f"{strings:>9}")

#   "%-9s"
print(f"{strings:<09}")

#   "%d%%"
print(f"{number_2:.0%}")