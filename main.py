import features

word = u'z\u016bgusyaa'

consonant_proportion = features.consonant_proportion(word)
print "consonant proportion for %s: %.2f" % (word, consonant_proportion)

vowel_proportion = features.vowel_proportion(word)
print "vowels proportion for %s: %.2f" % (word, vowel_proportion)

word = u'\u012blvi'
obstruent_proportion = features.obstruent_proportion(word)
print "obstruent proportion for %s: %.2f" % (word, obstruent_proportion)

