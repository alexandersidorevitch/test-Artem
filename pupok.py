import string
from random import choice

answers = [choice(string.ascii_lowercase) for i in range(100)]
print(*answers)

