import random


def resample_text(text, lengths=(1, 5)):
    """Generate next query as a piece of the current text.
    Possible options:
    - one of the quoted substrings # todo: implement it
    - a random substring
    - a tail of the text (with higher probability) # todo: implement it
    """
    tokens = text.split()
    n = random.randint(*lengths)
    position = random.randint(0, max(0, len(tokens) - n))
    return ' '.join(tokens[position:(position+n)])
