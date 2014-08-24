from features import proportion,coda,clusters

word = u'z\u016bgusyaa'
consonant_proportion = proportion.consonant_proportion(word)
print "consonant proportion for %s: %.2f" % (word, consonant_proportion)
vowel_proportion = proportion.vowel_proportion(word)
print "vowels proportion for %s: %.2f" % (word, vowel_proportion)

word = u'\u012blvi'
obstruent_proportion = proportion.obstruent_proportion(word)
print "obstruent proportion for %s: %.2f" % (word, obstruent_proportion)

word = u'lysoon'
consonant_coda = coda.consonant_coda(word)
print "consonant coda for %s: %i" % (word, consonant_coda)
obstruent_coda = coda.obstruent_coda(word)
print "obstruent coda for %s: %i" % (word, obstruent_coda)

word = u'avvirsosh'
consonant_clusters = clusters.consonant_clusters(word)
print "consonant clusters for %s: %i" % (word, consonant_clusters)
obstruent_clusters = clusters.obstruent_clusters(word)
print "consonant clusters for %s: %i" % (word, obstruent_clusters)

word = u'haeshi'
vowel_clusters = clusters.vowel_clusters(word)
print "vowel clusters for %s: %i" % (word, vowel_clusters)
