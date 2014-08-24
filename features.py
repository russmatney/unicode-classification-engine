CONSONANTS_REGEX = u'bcdfgjklmnpqrstvxz\u00f1'
OBSTRUENT_REGEX = u'bcdfgjkpqstvxz'

def consonant_proportion(word):
  converse = False
  return x_proportion(CONSONANTS_REGEX, word, converse)

#For now, this assumes vowels are the converse of the consonants regex
def vowel_proportion(word):
  converse = True
  return x_proportion(CONSONANTS_REGEX, word, converse)

def obstruent_proportion(word):
  converse = False
  return x_proportion(OBSTRUENT_REGEX, word, converse)

def x_proportion(regex, word, converse):
  count = 0
  for letter in regex:
  	count += word.count(letter)
  average = float(count) / len(word)
  if converse: average = get_converse(average)
  return average

def get_converse(ratio):
  return 1 - ratio
