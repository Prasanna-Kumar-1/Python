#  difflib.get_close_matches returns a list of the best “good enough” matches.
#  This script is to demonstrate that

from difflib import get_close_matches

names = ['julian', 'pythonista', 'sara']
print(get_close_matches('python', names))
print(get_close_matches('jul', names))
print(get_close_matches('ara', names))

