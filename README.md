#unicode-classification-engine

An abstraction of some techniques for distinguishing two texts,
based on typical Linguistic techniques.

This engine lets you run a few standard analyses of any (Unicode) corpus,
or create your own.

For a quick demo, run:

```python
python main.py
```

##Features

- Consonant, Obstruent, Vowel proportion per word
- Consonant, Obstruent Coda
- Consonant, Obstruent, Vowel clusters

##Usage:

```python
from features import coda

word = u'lysoon'
consonant_coda = coda.consonant_coda(word)

print "consonant coda for %s: %i" % (word, consonant_coda)
```

##Unit tests:

To run the unit tests, just run `python -m unittest discover test '*_test.py'`.

##TODO:

- Importing Raw Text
- Clean up
- Tokenizing
- Lexical Distribution
- Unit Tests
