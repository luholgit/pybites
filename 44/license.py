import random
from string import ascii_uppercase, digits


def gen_key(parts: int = 4, chars_per_part: int = 8):
    key_parts = []
    for _ in range(parts):
        key_parts.append(
            "".join(random.choices(population=ascii_uppercase + digits, k=chars_per_part))
        )

    key = "-".join(key_parts)

    return key
