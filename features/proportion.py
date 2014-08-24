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

##Generic
def proportion(regex, word, converse):
  count = 0
  for letter in regex:
  	count += word.count(letter)
  length = len(word)
  if length is 0: return 0
  average = float(count) / length
  if converse: average = get_converse(average)
  return average

def get_converse(ratio):
  return 1 - ratio
