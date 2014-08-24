CONSONANTS_REGEX = u'bcdfgjklmnpqrstvxz\u00f1'

def consonants_per_word(word):
  return x_per_word(word, CONSONANTS_REGEX, False)

def vowels_per_word(word):
  return x_per_word(word, CONSONANTS_REGEX, True)

def x_per_word(word, regex, inverse):
  count = 0
  for letter in regex:
  	count += word.count(letter)
  average = float(count) / len(word)
  if inverse:
  	average = 1 - average
  return average
