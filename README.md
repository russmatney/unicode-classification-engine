#unicode-classification-engine

An abstraction of some techniques for distinguishing two texts,
based on typical Linguistic techniques.

This engine lets you run a few standard analyses of any (Unicode) corpus,
or create your own.

##Features

- Consonant, Obstruent, Vowel proportion per word
- Consonant, Obstruent Coda
- Consonant, Obstruent, Vowel clusters

##Usage:

```python
import features

word = u'lysoon'
consonant_coda = features.consonant_coda(word)

print "consonant coda for %s: %i" % (word, consonant_coda)
```

##Unit tests:

To run the unit tests, just run `python features_test.py`.

##TODO:

- Importing Raw Text
- Clean up
- Tokenizing
- Lexical Distribution
