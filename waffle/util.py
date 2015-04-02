import random

def generate_name():
    words = open('/usr/share/dict/words', 'r').read().splitlines()
    return '-'.join([random.choice(words) for _ in range(3)])
