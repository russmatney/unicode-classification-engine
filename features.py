import re

CONSONANTS_REGEX = u'bcdfgjklmnpqrstvxz\u00f1'
OBSTRUENT_REGEX = u'bcdfgjkpqstvxz'

def consonant_proportion(word):
  converse = False
  return proportion(CONSONANTS_REGEX, word, converse)

#For now, this assumes vowels are the converse of the consonants regex
def vowel_proportion(word):
  converse = True
  return proportion(CONSONANTS_REGEX, word, converse)

def obstruent_proportion(word):
  converse = False
  return proportion(OBSTRUENT_REGEX, word, converse)

def proportion(regex, word, converse):
  count = 0
  for letter in regex:
  	count += word.count(letter)
  average = float(count) / len(word)
  if converse: average = get_converse(average)
  return average

def get_converse(ratio):
  return 1 - ratio

def consonant_coda(word):
  return coda(CONSONANTS_REGEX, word)
def obstruent_coda(word):
  return coda(OBSTRUENT_REGEX, word)

def coda(regex, word):
  if word[-1] in regex: return 1
  else: return 0

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

