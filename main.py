import features

word = u'z\u016bgusyaa'
consonant_proportion = features.consonant_proportion(word)
print "consonant proportion for %s: %.2f" % (word, consonant_proportion)
vowel_proportion = features.vowel_proportion(word)
print "vowels proportion for %s: %.2f" % (word, vowel_proportion)

word = u'\u012blvi'
obstruent_proportion = features.obstruent_proportion(word)
print "obstruent proportion for %s: %.2f" % (word, obstruent_proportion)

word = u'lysoon'
consonant_coda = features.consonant_coda(word)
print "consonant coda for %s: %i" % (word, consonant_coda)
obstruent_coda = features.obstruent_coda(word)
print "obstruent coda for %s: %i" % (word, obstruent_coda)
