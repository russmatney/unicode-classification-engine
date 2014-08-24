import re
from constants import *

def consonant_clusters(word):
  return clusters(CONSONANTS_REGEX, word)

def obstruent_clusters(word):
  return clusters(OBSTRUENT_REGEX, word)

def clusters(regex, word):
  regex = ur'[' + regex + '][' + regex + ']+'
  set = re.findall(regex, word, re.UNICODE)
  return len(set)

#Slightly different algorithm
def vowel_clusters(word):
  set = re.split(CONSONANTS_REGEX, word, re.UNICODE)
  vowel_set = [v for v in set if len(v) > 1]
  return len(vowel_set)
