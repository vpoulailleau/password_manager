# https://en.wikipedia.org/wiki/Linear_congruential_generator glibc
_MODULUS = 1 << 31
_MULTIPLIER = 1103515245
_INCREMENT = 12345

_prng = 0


def srand(seed: int) -> None:
    global _prng
    _prng = seed


def rand() -> int:
    global _prng
    _prng = (_MULTIPLIER * _prng + _INCREMENT) % _MODULUS
    return _prng & 0x7FFFFFFF
