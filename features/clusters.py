import re
from constants import *

def consonant_clusters(word):
  regex = ur'[' + CONSONANTS_REGEX + '][' + CONSONANTS_REGEX + ']+'
  return clusters(regex, word)

def obstruent_clusters(word):
  regex = ur'[' + OBSTRUENT_REGEX + '][' + OBSTRUENT_REGEX + ']+'
  return clusters(regex, word)

def vowel_clusters(word):
  set = re.split(CONSONANTS_REGEX, word, re.UNICODE)
  vowel_set = [v for v in set if len(v) > 1]
  return len(vowel_set)

def clusters(regex, word):
  set = re.findall(regex, word, re.UNICODE)
  return len(set)

