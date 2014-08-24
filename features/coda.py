from constants import *

def consonant_coda(word):
  return coda(CONSONANTS_REGEX, word)
def obstruent_coda(word):
  return coda(OBSTRUENT_REGEX, word)

def coda(regex, word):
  if word[-1] in regex: return 1
  else: return 0


